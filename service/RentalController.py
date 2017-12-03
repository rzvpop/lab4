from datetime import date, timedelta

from domain.book import Book
from domain.client import Client
from domain.exceptions import LibraryException
from domain.rental import Rental
from service import Controller
from service.Controller import ItemController


class RentalController(ItemController):
    def __init__(self, repo, book_repo, client_repo):
        ItemController.__init__(self, repo)
        self.__book_repo = book_repo
        self.__client_repo = client_repo

    def avlBook(self, book_id):
        rentals = self._repo.getAll()
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
            self._validator.rentalValidator(r)
            try:
                self._repo.add(r)
            except LibraryException:
                raise LibraryException("There already is a rental with this id!")
        else:
            raise LibraryException("This book is not available!")

    def getRentals(self):
        return self._repo.getAll()

    def updateRental(self, args):
        r = Rental(int(args[0]), int(args[1]), int(args[2]), args[3], args[4], args[5])
        self._validator.rentalValidator(r)
        self._repo.upd(r)

    def returnBook(self, args):
        r = Rental(int(args[0]), 1, 1, date.today(), date.today(), False)
        r = self._repo.find(r)
        self._validator.rentalValidator(r)
        r.retDate = date.today()
