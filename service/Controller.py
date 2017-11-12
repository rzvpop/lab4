from datetime import date, datetime

from domain.book import Book
from domain.client import Client
from domain.exceptions import LibraryException
from domain.rental import Rental
from repository.Repository import Repository
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
        b = Book(int(id), "default", "default", "default")
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
        c = Client(int(id), "default")
        self.__validator.validateClient(c)
        self.__client_repo.rem(c)

    def updateClient(self, args):
        c = Client(int(args[0]), args[1])
        self.__validator.validateClient(c)
        self.__client_repo.upd(c)

    def isAvailable(self, book_id):
        rentals = self.__book_repo.getAll()
        for x in rentals:
            if x.book_id == book_id:
                state = x.rentState()
                if state["ret"] == False:
                    return False
        return False

    def addRental(self, args):
        if self.isAvailable(args[1]):
            r = Rental(int(args[0]), int(args[1]), int(args[2]), datetime.strptime(args[3], "%Y-%m-%d"), datetime.strptime(args[4], "%Y-%m-%d"), datetime.strptime(args[5], "%Y-%m-%d"))
            self.__validator.rentalValidator(r)
            self.__rental_repo.add(r)
        else:
            raise LibraryException("This book is not available!")


def testAddRent():
    repo = Repository()

    #repo.add(1, 2, 3, )