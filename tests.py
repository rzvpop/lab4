from domain.book import Book
import unittest
from repository.Repository import Repository
from service.StatisticsController import StatisticsController


class testBook(unittest.TestCase):

    def test_book(self):
        b = Book(1, "Fizica", "fiction", "Ilea Carmen")
        self.assertTrue(b.title == "Fizica")

class testStatController(unittest.TestCase):
    def test_search(self):
        book_repo = Repository()
        client_repo = Repository()
        rental_repo = Repository()
        book_repo.add(Book(1, "Iona", "teatru postbelic", "Marin Sorescu"))
        book_repo.add(Book(2, "Amintiri din copilarie", "proza", "Ion Creanga"))
        book_repo.add(Book(3, "1984", "roman", "George Orwell"))

        st_ctrl = StatisticsController(book_repo, client_repo, rental_repo)
        l = st_ctrl.search(book_repo, "author", "re")

        self.assertTrue(len(l) == 2)



if __name__ == "__main__":
    unittest.main()