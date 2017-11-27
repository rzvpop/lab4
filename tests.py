from domain.book import Book
import unittest

class testBook(unittest.TestCase):

    def test_book(self):
        b = Book(1, "Fizica", "fiction", "Ilea Carmen")
        print(b.title)
        self.assertTrue(b.title == "Fizica")

if __name__ == "__main__":
    unittest.main()