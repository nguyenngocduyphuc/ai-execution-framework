"""Main application module."""
from fastapi import FastAPI

app = FastAPI()

@app.get("/health")
async def health_check():
    return {"status": "ok"}

@app.get("/items")
async def read_items():
    return [{"id": 1, "name": "Item 1"}]

@app.post("/items")
async def create_item(name: str):
    return {"name": name, "id": 1}
