import pytest
from fastapi.testclient import TestClient
from app.main import app 

client = TestClient(app)

def test_redirect_to_not_found():
    response = client.get("/non-existing-path")
    assert response.status_code == 404
    assert str(response.url).endswith("/not-found")
