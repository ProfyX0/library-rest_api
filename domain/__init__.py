class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.count = 1
    def increase_count(self):
        self.count += 1
    title: str
    author: str
    count: int