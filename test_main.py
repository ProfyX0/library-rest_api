from fastapi.testclient import TestClient

from main import app
client = TestClient(app)

def test_read_main():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello Library"}

def test_read_books():
    response = client.get("/books")
    assert response.status_code == 200

def test_create_books():
    response = client.post("/books", json={"title": "Skripta MA2", "author": "Tomas Kalvoda"})
    assert response.status_code == 200
    assert response.json() == {"title": "Skripta MA2", "author": "Tomas Kalvoda"}

def test_create_same_book_twice():
    response = client.post("/books", json={"title": "Skripta MA1", "author": "Tomas Kalvoda"})
    assert response.status_code == 200
    assert response.json() == {"title": "Skripta MA1", "author": "Tomas Kalvoda"}
    response = client.post("/books", json={"title": "Skripta MA1", "author": "Tomas Kalvoda"})
    assert response.status_code == 200
    assert response.json() == {"title": "Skripta MA1", "author": "Tomas Kalvoda"}

def test_author_report():
    response = client.get("/authors/report")
    assert response.status_code == 200

def test_invalid_url():
    response = client.get("/invalid")
    assert response.status_code == 404
