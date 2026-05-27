#!/usr/bin/env python3
"""
AXF Asana Bridge (Anthropic-Style Automation)
Connects local task.md YAML frontmatter to Asana API.

Usage:
    python scripts/axf_asana.py create <task.md>
    python scripts/axf_asana.py update <task.md> --status done --evidence <url>
    python scripts/axf_asana.py list
"""

import os
import sys
import json
import time
import argparse
import subprocess
from pathlib import Path

# Check for PyYAML
try:
    import yaml
except ImportError:
    print("❌ PyYAML is required. Install via: pip install pyyaml")
    sys.exit(1)

import requests

# Config
ASANA_TOKEN = os.environ.get("ASANA_TOKEN")
ASANA_CONFIG_PATH = Path(__file__).parent.parent / "config" / "asana_config.json"

def load_config():
    """Load workspace/project GIDs from config."""
    if not ASANA_CONFIG_PATH.exists():
        print("❌ Missing config/asana_config.json")
        sys.exit(1)
    with open(ASANA_CONFIG_PATH, "r") as f:
        return json.load(f)

def parse_task_md(path):
    """Parse YAML frontmatter from task.md using PyYAML."""
    with open(path, "r") as f:
        content = f.read()
    
    match = content.split("---")
    if len(match) < 3:
        print("❌ No YAML frontmatter found in task.md")
        sys.exit(1)
    
    try:
        task = yaml.safe_load(match[1])
        if not isinstance(task, dict):
            print("❌ Invalid YAML format in task.md")
            sys.exit(1)
        return task
    except yaml.YAMLError as e:
        print(f"❌ YAML parsing error: {e}")
        sys.exit(1)

def asana_api_request(method, url, headers, payload=None):
    """Robust API request with retry logic."""
    for attempt in range(3):
        try:
            resp = requests.request(method, url, json=payload, headers=headers)
            if resp.status_code == 429:
                retry_after = int(resp.headers.get('Retry-After', 10))
                print(f"⏳ Rate limited. Retrying in {retry_after}s...")
                time.sleep(retry_after)
                continue
            return resp
        except requests.exceptions.RequestException as e:
            print(f"❌ Network error: {e}")
            if attempt < 2:
                time.sleep(5)
            else:
                sys.exit(1)
    return None

def create_task(task_md_path):
    """Create Asana task from task.md."""
    if not ASANA_TOKEN:
        print("❌ ASANA_TOKEN not set in environment.")
        sys.exit(1)
    
    config = load_config()
    task = parse_task_md(task_md_path)
    
    headers = {"Authorization": f"Bearer {ASANA_TOKEN}"}
    payload = {
        "data": {
            "name": task.get("title", "Untitled Task"),
            "notes": task.get("goal", ""),
            "projects": [config["project_gid"]],
            "workspace": config["workspace_gid"]
        }
    }
    
    print(f"📤 Creating task in Asana: {payload['data']['name']}...")
    resp = asana_api_request("POST", "https://app.asana.com/api/1.0/tasks", headers, payload)
    
    if resp and resp.status_code == 201:
        asana_task = resp.json()["data"]
        asana_gid = asana_task["gid"]
        asana_url = asana_task["permalink"]
        
        print(f"✅ Created: {asana_url}")
        
        # Inject GID back into task.md safely using YAML dump
        task["asana_gid"] = asana_gid
        task["asana_url"] = asana_url
        
        # Reconstruct file
        match = open(task_md_path).read().split("---")
        new_fm = yaml.dump(task, default_flow_style=False)
        new_content = f"---\n{new_fm}---\n{'---'.join(match[2:])}"
        
        with open(task_md_path, "w") as f:
            f.write(new_content)
        print("📝 Injected asana_gid into task.md")
    else:
        print(f"❌ Failed: {resp.text if resp else 'No response'}")

def update_task(task_md_path, status, evidence, done):
    """Update Asana task status and add evidence comment."""
    if not ASANA_TOKEN:
        print("❌ ASANA_TOKEN not set in environment.")
        sys.exit(1)
    
    task = parse_task_md(task_md_path)
    asana_gid = task.get("asana_gid")
    
    if not asana_gid:
        print("❌ No asana_gid found in task.md. Run 'create' first.")
        sys.exit(1)
    
    headers = {"Authorization": f"Bearer {ASANA_TOKEN}"}
    
    # 1. Update Status (Mark as completed if --done flag is set)
    if done:
        payload = {"data": {"completed": True}}
        resp = asana_api_request("PUT", f"https://app.asana.com/api/1.0/tasks/{asana_gid}", headers, payload)
        if resp and resp.status_code == 200:
            print("✅ Task marked as Completed in Asana.")
        else:
            print(f"⚠️ Failed to mark completed: {resp.text if resp else 'No response'}")
    
    # 2. Add Evidence Comment
    comment_text = f"🤖 AXF Agent Update:\nStatus: {status}\nEvidence: {evidence}"
    payload = {"data": {"text": comment_text}}
    resp = asana_api_request("POST", f"https://app.asana.com/api/1.0/tasks/{asana_gid}/stories", headers, payload)
    
    if resp and resp.status_code == 201:
        print(f"✅ Attached evidence to Asana Task {asana_gid}.")
    else:
        print(f"⚠️ Failed to attach evidence: {resp.text if resp else 'No response'}")

def list_tasks():
    """List tasks assigned to current agent in Asana."""
    if not ASANA_TOKEN:
        print("❌ ASANA_TOKEN not set in environment.")
        sys.exit(1)
    
    config = load_config()
    headers = {"Authorization": f"Bearer {ASANA_TOKEN}"}
    
    # Get user GID first
    user_resp = asana_api_request("GET", "https://app.asana.com/api/1.0/users/me", headers)
    if not user_resp or user_resp.status_code != 200:
        print(f"❌ Failed to get user info: {user_resp.text if user_resp else 'No response'}")
        return
    user_gid = user_resp.json()["data"]["gid"]
    
    # Get tasks
    params = {"assignee": user_gid, "project": config["project_gid"]}
    resp = asana_api_request("GET", "https://app.asana.com/api/1.0/tasks", headers, params)
    
    if resp and resp.status_code == 200:
        tasks = resp.json()["data"]
        print(f"📋 Found {len(tasks)} tasks:")
        for t in tasks:
            status = "✅ Done" if t.get('completed') else "⏳ In Progress"
            print(f"  - {status} | {t['name']} ({t['permalink']})")
    else:
        print(f"❌ Failed to list tasks: {resp.text if resp else 'No response'}")

def main():
    parser = argparse.ArgumentParser(description="AXF Asana Bridge")
    subparsers = parser.add_subparsers(dest="command")
    
    # Create
    create_parser = subparsers.add_parser("create", help="Create Asana task from task.md")
    create_parser.add_argument("task_md", help="Path to task.md")
    
    # Update
    update_parser = subparsers.add_parser("update", help="Update Asana task")
    update_parser.add_argument("task_md", help="Path to task.md")
    update_parser.add_argument("--status", default="In Progress")
    update_parser.add_argument("--evidence", required=True)
    update_parser.add_argument("--done", action="store_true", help="Mark task as completed")
    
    # List
    subparsers.add_parser("list", help="List assigned tasks")
    
    args = parser.parse_args()
    
    if args.command == "create":
        create_task(args.task_md)
    elif args.command == "update":
        update_task(args.task_md, args.status, args.evidence, args.done)
    elif args.command == "list":
        list_tasks()
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
