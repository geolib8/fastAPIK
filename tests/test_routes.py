from fastapi.testclient import TestClient
from app import app

client = TestClient(app)

def test_get_all_todos():
    response = client.get("/")
    assert response.status_code == 200
    assert "data" in response.json()

def test_create_todo():
    todo_data = {
        "name": "Test Todo",
        "description": "This is a test todo",
        "complete": False
    }
    response = client.post("/", json=todo_data)
    assert response.status_code == 201
    assert response.json()["message"] == "Todo created successfully"

def test_update_todo():
    # Replace 'todo_id' with a valid ID from your database
    todo_id = "64a7dcdc56d7c60c442e2a44"
    todo_data = {
        "name": "Updated Todo",
        "description": "This is an updated test todo",
        "complete": True
    }
    response = client.put(f"/{todo_id}", json=todo_data)
    assert response.status_code == 200

def test_delete_todo():
    # Replace 'todo_id' with a valid ID from your database
    todo_id = "64a7dcdc56d7c60c442e2a44"
    response = client.delete(f"/{todo_id}")
    assert response.status_code == 200
    assert response.json()["message"] == "Todo deleted successfully"
