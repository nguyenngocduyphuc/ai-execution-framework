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
import re
import requests
import argparse
from pathlib import Path

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
    """Parse YAML frontmatter from task.md."""
    with open(path, "r") as f:
        content = f.read()
    
    match = re.search(r"---\n(.*?)\n---", content, re.DOTALL)
    if not match:
        print("❌ No YAML frontmatter found in task.md")
        sys.exit(1)
    
    fm = match.group(1)
    task = {}
    
    # Simple YAML parser for our specific structure
    for line in fm.split("\n"):
        if ":" in line:
            key, val = line.split(":", 1)
            task[key.strip()] = val.strip().strip('"')
    
    return task

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
    resp = requests.post("https://app.asana.com/api/1.0/tasks", json=payload, headers=headers)
    
    if resp.status_code == 201:
        asana_task = resp.json()["data"]
        asana_gid = asana_task["gid"]
        asana_url = asana_task["permalink"]
        
        print(f"✅ Created: {asana_url}")
        
        # Inject GID back into task.md
        with open(task_md_path, "r") as f:
            content = f.read()
        
        # Add asana_gid if not exists
        if "asana_gid" not in content:
            content = content.replace("---", f"---\nasana_gid: {asana_gid}", 1)
            content = content.replace("---", f"---\nasana_url: {asana_url}", 1)
            with open(task_md_path, "w") as f:
                f.write(content)
            print("📝 Injected asana_gid into task.md")
    else:
        print(f"❌ Failed: {resp.text}")

def update_task(task_md_path, status, evidence):
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
    
    # 1. Update Status (via custom field or notes for now)
    # Note: Asana status updates usually require custom fields. 
    # For simplicity, we'll add a comment and update notes.
    comment_text = f"🤖 AXF Agent Update:\nStatus: {status}\nEvidence: {evidence}"
    
    payload = {"data": {"text": comment_text}}
    resp = requests.post(f"https://app.asana.com/api/1.0/tasks/{asana_gid}/stories", json=payload, headers=headers)
    
    if resp.status_code == 201:
        print(f"✅ Updated Asana Task {asana_gid} with evidence.")
    else:
        print(f"❌ Failed to update: {resp.text}")

def list_tasks():
    """List tasks assigned to current agent in Asana."""
    if not ASANA_TOKEN:
        print("❌ ASANA_TOKEN not set in environment.")
        sys.exit(1)
    
    config = load_config()
    headers = {"Authorization": f"Bearer {ASANA_TOKEN}"}
    
    # Get user GID first
    user_resp = requests.get("https://app.asana.com/api/1.0/users/me", headers=headers)
    user_gid = user_resp.json()["data"]["gid"]
    
    # Get tasks
    params = {"assignee": user_gid, "project": config["project_gid"]}
    resp = requests.get("https://app.asana.com/api/1.0/tasks", params=params, headers=headers)
    
    if resp.status_code == 200:
        tasks = resp.json()["data"]
        print(f"📋 Found {len(tasks)} tasks:")
        for t in tasks:
            print(f"  - [{t['completed']}] {t['name']} ({t['permalink']})")
    else:
        print(f"❌ Failed to list tasks: {resp.text}")

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
    
    # List
    subparsers.add_parser("list", help="List assigned tasks")
    
    args = parser.parse_args()
    
    if args.command == "create":
        create_task(args.task_md)
    elif args.command == "update":
        update_task(args.task_md, args.status, args.evidence)
    elif args.command == "list":
        list_tasks()
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
