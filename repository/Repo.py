from domain.book import Book


class BookRepo():
    def __init__(self):
        self._data = []

    def add(self, b):
        if isinstance(b, Book):
            self._data.append(b)
        else:
            raise TypeError("Non-book object can't be added to the repository!")

