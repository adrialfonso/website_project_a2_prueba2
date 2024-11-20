import pytest
from fastapi.testclient import TestClient
from app.main import app 

client = TestClient(app)

@pytest.fixture
def mock_database():
    pass

def test_read_top5_matched_books(mock_database):
    keyword = "The"
    response = client.get(f"/api/v1/books/{keyword}")

    assert response.status_code == 200
    assert response.headers["content-type"] == "application/json"

    data = response.json()

    assert "data" in data
    assert isinstance(data["data"], list)
    assert len(data["data"]) <= 5 

    for book in data["data"]:
        assert "id_book" in book
        assert "title" in book
        assert "authors" in book
        assert "synopsis" in book
        assert "buy_link" in book
        assert "genres" in book
        assert "rating" in book
        assert "editorial" in book
        assert "comments" in book
        assert "publication_date" in book
        assert "image" in book

    assert "count" in data
    assert isinstance(data["count"], int)

def test_filter_books_by_genres(mock_database):
    genres = ["Fiction", "Adventure"]

    response = client.post("/api/v1/books/filter-by-genres", json=genres)
    assert response.status_code == 200
    assert response.headers["content-type"] == "application/json"

    data = response.json()
    assert "data" in data
    assert "count" in data

    assert isinstance(data["data"], list)

    for book in data["data"]:
        assert "id_book" in book
        assert "title" in book
        assert "authors" in book
        assert "synopsis" in book
        assert "buy_link" in book
        assert "genres" in book
        assert "rating" in book
        assert "editorial" in book
        assert "comments" in book
        assert "publication_date" in book
        assert "image" in book

    assert isinstance(data["count"], int)
    assert data["count"] >= len(data["data"]) 

