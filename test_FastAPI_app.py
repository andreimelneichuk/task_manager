from fastapi.testclient import TestClient
from FastAPI_app import app

client = TestClient(app)

def test_get_user():
    response = client.get("/user/1")
    assert response.status_code == 200
    assert "user" in response.json()