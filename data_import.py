import pandas as pd

from domain import Book

def import_data():
    path = input("Enter path to csv file: ").strip()
    books = pd.read_csv(path, delimiter=';')
    dict_books = dict()
    for index, row in books.iterrows():
        author = row['Author']
        book_title = row['Book Title']
        book = Book(book_title, author)

        dict_books = add_book_to_dict(dict_books, book)
    return dict_books

def add_book_to_dict(dict_books, book):
    author = book.author
    book_title = book.title

    if author not in dict_books:
        dict_books[author] = set()
    set_books = dict_books.get(author)
    found_book = False
    for b in set_books:
        if b.title == book_title:
            b.increase_count()
            found_book = True
            break
    if not found_book:
        set_books.add(book)
        dict_books[author] = set_books
    return dict_books