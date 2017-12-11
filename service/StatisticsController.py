from domain.book import Book
from domain.rental import Rental
from repository.Repository import RepositoryException


class StatisticsController():
    def __init__(self, book_repo, client_repo, rental_repo, undo_ctrl):
        self.__book_repo = book_repo
        self.__client_repo = client_repo
        self.__rental_repo = rental_repo
        self.__undo_ctrl = undo_ctrl

    def search(self, repo, attr, p_str, l):
        '''
            Finds objects in repository by partially matching of a specified string-type attribute.
            In: repo(repository), attr(string - name o f attribute), p_str(string)
            Out: l(list of objects)
        '''

        items = repo.getAll()

        for x in items:
            try:
                attr_value = getattr(x, attr)
                attr_value = attr_value.lower()
            except:
                raise RepositoryException("Book has such attribute.")
            if p_str in attr_value:
                if x not in l:
                    l.append(x)

        return l

    def bookSearch(self, hint):
        l = []
        self.search(self.__book_repo, "title", hint, l)
        self.search(self.__book_repo, "author", hint, l)
        self.search(self.__book_repo, "desc", hint, l)
        if len(l) > 0:
            return l
        else:
            raise RepositoryException("No books found.")

    def clientSearch(self, hint):
        l = []
        self.search(self.__client_repo, "name", hint, l)
        if len(l) > 0:
            return l
        else:
            raise RepositoryException("No clients found.")


    def mostRentedBooks(self):
        l = {}
        rentals = self.__rental_repo.getAll()

        for x in rentals:
            if x.bookId not in l:
                l[x.bookId] = 1
            else:
                l[x.bookId] += 1

        nr_rentals = []
        for x in l.keys():
            nr_rentals.append([self.__book_repo.find(Book(x, "def", "def", "def")), l[x]])

        nr_rentals.sort(key=lambda x: x[1], reverse=True)

        return nr_rentals

