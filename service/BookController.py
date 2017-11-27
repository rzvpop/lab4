from datetime import date, datetime, timedelta

from domain.book import Book
from domain.client import Client
from domain.exceptions import LibraryException
from domain.rental import Rental
from repository.Repository import Repository
from service.Controller import Controller
from validation.Validator import Validator

class BookController(Controller):
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