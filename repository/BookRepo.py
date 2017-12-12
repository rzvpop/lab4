from domain.book import Book
from repository.Repository import Repository, RepositoryException


class BookFileRepository(Repository):
    def __init__(self, f_name="books.txt"):
        Repository.__init__(self)
        self.__f_name = f_name
        self.__loadFromFile()

    def add(self, book):
        Repository.add(self, book)
        self.__storeToFile()

    def rem(self, book):
        Repository.rem(self, book)
        self.__storeToFile()

    def upd(self, book):
        Repository.upd(self, book)
        self.__storeToFile()

    def __loadFromFile(self):
        try:
            f = open(self.__f_name, "r")
            line = f.readline().strip()
            while line != "":
                attrs = line.split(',')
                b = Book(int(attrs[0]), attrs[1], attrs[2], attrs[3])
                Repository.add(self, b)
                line = f.readline().strip()
        except IOError:
            raise RepositoryException("Can't load data from file " + self.__f_name + "!")
        f.close()

    def __storeToFile(self):
        f = open(self.__f_name, "w")
        books = Repository.getAll(self)

        for book in books:
            str_book = str(book.id) + ", " + book.title + ", " + book.desc + ", " + book.author + "\n"
            f.write(str_book)

        f.close()