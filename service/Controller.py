from domain.book import Book
from domain.client import Client
from validation.Validator import Validator


class Controller():
    def __init__(self, book_repo, client_repo, rental_repo):
        self.__book_repo = book_repo
        self.__client_repo = client_repo
        self.__rental_repo = rental_repo
        self.__validator = Validator()

    def addBook(self, args):
        b = Book(int(args[0]), args[1], args[2], args[3])
        self.__validator.validateBook(b)
        self.__book_repo.add(b)

    def removeBook(self, id):
        b = Book(id, "default", "default", "default")
        self.__validator.validateBook(b)
        self.__book_repo.rem(b)

    def updateBook(self, args):
        b = Book(int(args[0]), args[1], args[2], args[3])
        self.__validator.validateBook(b)
        self.__book_repo.upd(b)

    def getBooks(self):
        return self.__book_repo.getAll()

    def addClient(self, args):
        c = Client(int(args[0]), args[1])
        self.__validator.validateClient(c)
        self.__client_repo.add(c)

    def getClients(self):
        return self.__client_repo.getAll()

    def removeClient(self, id):
        c = Client(id, "default")
        self.__validator.validateClient(c)
        self.__client_repo.rem(c)

    def updateClient(self, args):
        c = Client(int(args[0]), args[1])
        self.__validator.validateClient(c)
        self.__client_repo.upd(c)
