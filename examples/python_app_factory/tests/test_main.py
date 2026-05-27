"""Tests for main application."""
from fastapi.testclient import TestClient
from src.main import app

client = TestClient(app)

def test_health_check():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}

def test_read_items():
    response = client.get("/items")
    assert response.status_code == 200
    assert len(response.json()) > 0

def test_create_item():
    response = client.post("/items?name=test")
    assert response.status_code == 200
    assert response.json()["name"] == "test"
