from datetime import date, timedelta

from domain.book import Book
import unittest

from domain.client import Client
from domain.rental import Rental
from repository.Repository import Repository
from service.StatisticsController import StatisticsController
from validation.Validator import Validator, ValidationException


class testBook(unittest.TestCase):

    def test_setGet(self):
        b = Book(1, "Fizica", "fiction", "Ilea Carmen")
        self.assertTrue(b.title == "Fizica")

        b.id = 2
        b.title = "Matematica"
        b.desc = "somehow human"
        b.author = "Ganga"

        self.assertTrue(b == Book(2, "Matematica", "somehow human", "Ganga"))


class testClient(unittest.TestCase):
    def test_setGet(self):
        c = Client(3, "Ivan Turbinca")
        self.assertTrue(c.name == "Ivan Turbinca")

        c.id = 3
        c.name = "Gigi Becali"

        self.assertTrue(3, "Gigi Becali")


class testRental(unittest.TestCase):
    def test_setGet(self):
        r = Rental(1, 4, 2, date(2017, 12, 5), date(2017, 12, 5) + timedelta(days=10), False)
        self.assertTrue(r.dueDate == date(2017, 12, 15))

        r.clientId = 10

        self.assertTrue(r.clientId == 10)


class testRentalController(unittest.TestCase):
    pass


class testStatController(unittest.TestCase):
    def test_search(self):
        book_repo = Repository()
        client_repo = Repository()
        rental_repo = Repository()
        book_repo.add(Book(1, "Iona", "teatru postbelic", "Marin Sorescu"))
        book_repo.add(Book(2, "Amintiri din copilarie", "proza", "Ion Creanga"))
        book_repo.add(Book(3, "1984", "roman", "George Orwell"))

        st_ctrl = StatisticsController(book_repo, client_repo, rental_repo)

        l = []
        st_ctrl.search(book_repo, "author", "re", l)
        self.assertTrue(len(l) == 2)

        rental_repo.add(Rental(2, 2, 10, date.today(), date.today() + timedelta(days=10), False))
        most_rented = st_ctrl.mostRentedBooks()
        self.assertTrue(most_rented[0] == [Book(2, "Amintiri din copilarie", "proza", "Ion Creanga"), 1])


class testValidator(unittest.TestCase):
    def testBookValidator(self):
        b = Book(1, "Arma invizibila", "", "Paul Feval")
        validator = Validator()

        try:
            validator.validateBook(b)
            self.assertTrue(False)
        except ValidationException as ve:
            self.assertTrue(str(ve) == "Invalid description!\n")

if __name__ == "__main__":
    unittest.main()