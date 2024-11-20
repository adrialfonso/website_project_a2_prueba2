import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_not_found_page():
    response = client.get("/not-found")
    assert response.status_code == 404 
    assert response.json() == {"detail": "Not Found"}  
