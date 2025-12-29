from fastapi.testclient import TestClient
from main import app

# This 'client' acts like a fake web browser for our code
client = TestClient(app)

def test_crud_lifecycle():
    # 1. TEST CREATE
    response = client.post("/items", json={"id": 1, "name": "Laptop", "quantity": 10})
    assert response.status_code == 201
    assert response.json()["item"]["name"] == "Laptop"

    # 2. TEST READ
    response = client.get("/items/1")
    assert response.status_code == 200
    assert response.json()["quantity"] == 10

    # 3. TEST UPDATE
    response = client.put("/items/1", json={"id": 1, "name": "Laptop", "quantity": 5})
    assert response.status_code == 200
    assert response.json()["item"]["quantity"] == 5

    # 4. TEST DELETE
    response = client.delete("/items/1")
    assert response.status_code == 200

    # 5. TEST READ (Confirm it is gone)
    response = client.get("/items/1")
    assert response.status_code == 404