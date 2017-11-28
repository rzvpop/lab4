from datetime import date, datetime, timedelta

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

    def avlBook(self, book_id):
        rentals = self.__rental_repo.getAll()
        for x in rentals:
            if x.bookId == book_id:
                state = x.rentState()
                if state["ret"] == False:
                    return False
        return True

    def addRental(self, args):
        if self.avlBook(int(args[1])):
            b = Book(int(args[1]), "default", "default", "default")
            try:
                self.__book_repo.find(b)
            except LibraryException:
                raise LibraryException("Inexistent book!")

            c = Client(int(args[2]), "default")
            try:
                self.__client_repo.find(c)
            except LibraryException:
                raise LibraryException("Unregistred client!")

            r = Rental(int(args[0]), int(args[1]), int(args[2]), date.today(), date.today() + timedelta(days=10), False)
            self.__validator.rentalValidator(r)
            try:
                self.__rental_repo.add(r)
            except LibraryException:
                raise LibraryException("There already is a rental with this id!")
        else:
            raise LibraryException("This book is not available!")

    def getRentals(self):
        return self.__rental_repo.getAll()

    def updateRental(self, args):
        r = Rental(int(args[0]), int(args[1]), int(args[2]), args[3], args[4], args[5])
        self.__validator.rentalValidator(r)
        self.__rental_repo.upd(r)

    def returnBook(self, args):
        r = Rental(int(args[0]), 1, 1, date.today(), date.today(), False)
        r = self.__rental_repo.find(r)
        self.__validator.rentalValidator(r)
        r.retDate = date.today()

    #def search(self, ):

def testBook():
    b_repo = Repository()

    b_repo.add(Book(1, "Charlie and the chocolate factory", "nice storry", "Roald Dalh"))
    b_repo.add(Book(3, "Ciresarii", "tat felu de aventuri", "Constantin Chirita"))

    return b_repo

def testClient():
    c_repo = Repository()

    c_repo.add(Client(2, "Sandu Ciorba"))
    c_repo.add(Client(12, "Ada Milea"))

    return c_repo

def testRent():
    b_repo = testBook()
    c_repo = testClient()
    r_repo = Repository()

    ctrl = Controller(b_repo, c_repo, r_repo)

    ctrl.addRental(["1", "3", "12"])
    try:
        ctrl.addRental(["2", "4", "42"])
    except LibraryException:
        pass

    rentals = r_repo.getAll()

    assert(rentals[0] == Rental(1, 4, 12, date.today(), date.today() + timedelta(days=10), False))

testRent()