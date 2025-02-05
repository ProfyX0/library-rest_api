from fastapi.testclient import TestClient
from data_import import *

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

def test_add_book():
    book = Book(title="Skripta MA2", author="Tomas Kalvoda")
    dict_books = {}
    dict_books = add_book_to_dict(dict_books, book)
    assert dict_books == {
        "Tomas Kalvoda": {book}
    }

def test_add_same_book_twice():
    book = Book(title="Skripta MA2", author="Tomas Kalvoda")
    dict_books = {}
    dict_books = add_book_to_dict(dict_books, book)
    dict_books = add_book_to_dict(dict_books, book)
    assert dict_books == {
        "Tomas Kalvoda": {book}
    }
    assert book.count == 2
