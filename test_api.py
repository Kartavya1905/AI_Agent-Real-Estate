from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_chat():
    response = client.post("/chat", json={"message": "Hello"})
    assert response.status_code == 200
    assert "response" in response.json()

def test_create_user():
    user = {
        "name": "Alice",
        "company": "Acme Inc",
        "email": "alice@acme.com"
    }
    response = client.post("/crm/create_user", json=user)
    assert response.status_code == 200
    assert response.json()["status"] == "User created using DB URI"
