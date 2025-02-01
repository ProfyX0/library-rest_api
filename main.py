from typing import Union
from fastapi import FastAPI
from pydantic import BaseModel
from data_import import import_data, add_book_to_dict
from domain import Book
import pandas as pd

books = import_data()

class BookModel(BaseModel):
    title: str
    author: str
app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello Library"}


@app.get("/books")
async def get_books_by_name(name: Union[str, None] = None):
    if name is None:
        return list(books.values())
    res = set()
    for set_book in books.values():
        for book in set_book:
            if name in book.author or name in book.title:
                res.add(book)
    return res

@app.post("/books")
async def add_book(book: BookModel):
    book_to_add = Book(book.title, book.author)
    add_book_to_dict(books, book_to_add)
    return book

@app.get("/authors/report")
async def author_report_by_books(sorted_by_absolute_count: bool = True):
    if sorted_by_absolute_count:
        sorted_dict = dict(sorted(books.items(), key=lambda x: sum(book.count for book in x[1]), reverse=True))
        ret = list(sorted_dict.keys())
        return {"authors:": ret}
    else:
        sorted_dict = dict(sorted(books.items(), key=lambda x: len(x[1]), reverse=True))
        ret = list(sorted_dict.keys())
        return {"authors:": ret}
