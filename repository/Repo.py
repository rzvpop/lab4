from domain.book import Book


class BookRepo():
    def __init__(self):
        self._data = []

    def add(self, b):
        if isinstance(b, Book):
            if b not in self._data:
                self._data.append(b)
            else:
                print("This id already exists!")
        else:
            raise TypeError("Non-book object can't be added to the repository!")

    def remove(self, b):
        if isinstance(b, Book):
            pass
        else:
            raise TypeError("Non-book object can't be removed from the repository!")

def testRepo():
    test_repo = BookRepo()
    b1 = Book(1, "10 little niggers", "detective fiction", "A.C.")
    b2 = Book(3, "The three musketeers", "adventure", "Alexandre Dumas")
    b3 = 23

    test_repo.add(b1)
    test_repo.add(b2)

    print(test_repo[1])
    #assert()