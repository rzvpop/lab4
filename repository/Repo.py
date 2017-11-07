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

    def remove(self, i):
        b = BookRepo.bookById(self, i)

        if b in self._data:
            self._data.remove(b)
        else:
            print("Could not find book!")


    def bookById(self, i):
        for x in self._data:
            if x.id == i:
                return x
        return False

    def update(self, args):
        b = BookRepo.bookById(self, args[0])
        if isinstance(b, Book):
            if args[1] != False:
                b.id = args[1]
            if args[2] != False:
                b.title = args[2]
            if args[3] != False:
                b.desc = args[3]
            if args[4] != False:
                b.author = args[4]
        else:
            print("Could not find book!")

    def __len__(self):
        return len(self._data)

    def __str__(self):
        s = "List of books:\n"
        for x in self._data:
            s = s + x.__str__() + '\n'
        return s

def testRepo():
    test_repo = BookRepo()
    b1 = Book(1, "10 little niggers", "detective fiction", "A.C.")
    b2 = Book(3, "The three musketeers", "adventure", "Alexandre Dumas")
    b3 = 23

    test_repo.add(b1)
    test_repo.add(b2)
    try:
        test_repo.add(b3)
    except TypeError as err:
        print(err)

    test_repo.update([3, False, False, "adventure fiction", False])

    test_repo.remove(1)

    print(test_repo)


testRepo()
