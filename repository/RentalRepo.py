from datetime import date, datetime

from domain.rental import Rental
from repository.Repository import Repository, RepositoryException


class RentalFileRepository(Repository):
    def __init__(self, f_name="rentals.txt"):
        Repository.__init__(self)
        self.__f_name = f_name
        self.__loadFromFile()

    def add(self, rental):
        Repository.add(self, rental)
        self.__storeToFile()

    def rem(self, rental):
        Repository.rem(self, rental)
        self.__storeToFile()

    def upd(self, rental):
        Repository.upd(self, rental)
        self.__storeToFile()

    def __loadFromFile(self):
        try:
            f = open(self.__f_name, "r")
            line = f.readline().strip()
            while line != "":
                attrs = line.split(',')
                attrs[3].strip(' ')
                attrs[3] = attrs[3].split('-')
                attrs[4].strip(' ')
                attrs[4] = attrs[4].split('-')
                attrs[5].strip(' ')
                if not attrs[5] == " False":
                    attrs[5] = attrs[5].split('-')
                    b = Rental(int(attrs[0]), int(attrs[1]), int(attrs[2]),
                               date(int(attrs[3][0]), int(attrs[3][1]), int(attrs[3][2])),
                               date(int(attrs[4][0]), int(attrs[4][1]), int(attrs[4][2])),
                               date(int(attrs[5][0]), int(attrs[5][1]), int(attrs[5][2])))
                else:
                    b = Rental(int(attrs[0]), int(attrs[1]), int(attrs[2]),
                               date(int(attrs[3][0]), int(attrs[3][1]), int(attrs[3][2])),
                               date(int(attrs[4][0]), int(attrs[4][1]), int(attrs[4][2])),
                               False)
                Repository.add(self, b)
                line = f.readline().strip()
        except IOError:
            raise RepositoryException("Can't load data from file " + self.__f_name + "!")
        f.close()

    def __storeToFile(self):
        f = open(self.__f_name, "w")
        rentals = Repository.getAll(self)

        for rental in rentals:
            str_book = str(rental.id) + ", " + str(rental.bookId) + ", " + str(rental.clientId) + ", " + str(rental.renDate) + ", " + str(rental.dueDate) + ", " + str(rental.retDate) + "\n"
            f.write(str_book)

        f.close()