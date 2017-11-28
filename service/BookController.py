from domain.book import Book
from service.Controller import ItemController


class BookController(ItemController):
    def addBook(self, args):
        b = Book(int(args[0]), args[1], args[2], args[3])
        self._validator.validateBook(b)
        self._repo.add(b)

    def removeBook(self, id):
        b = Book(int(id), "default", "default", "default")
        self._validator.validateBook(b)
        self._repo.rem(b)

    def updateBook(self, args):
        b = Book(int(args[0]), args[1], args[2], args[3])
        self._validator.validateBook(b)
        self._repo.upd(b)
