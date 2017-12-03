from datetime import date, datetime, timedelta

from domain.book import Book
from domain.client import Client
from domain.exceptions import LibraryException
from domain.rental import Rental
from repository.Repository import Repository
from validation.Validator import Validator


class ItemController():
    def __init__(self, repo):
        self._repo = repo
        self._validator = Validator()

    def getItems(self):
        return self._repo.getAll()

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

    ctrl = ItemController(b_repo, c_repo, r_repo)

    ctrl.addRental(["1", "3", "12"])
    try:
        ctrl.addRental(["2", "4", "42"])
    except LibraryException:
        pass

    rentals = r_repo.getAll()

    assert(rentals[0] == Rental(1, 4, 12, date.today(), date.today() + timedelta(days=10), False))

#testRent()