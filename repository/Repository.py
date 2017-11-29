from domain.exceptions import LibraryException


class RepositoryException(LibraryException):
    pass

class Repository:

    def __init__(self):
        self.__elems = []

    def add(self, elem):
        if elem in self.__elems:
            raise RepositoryException("Existent element!!")
        self.__elems.append(elem)

    def rem(self, elem):
        if elem not in self.__elems:
            raise RepositoryException("Inexistent element!!")
        self.__elems.remove(elem)

    def upd(self, elem):
        if elem not in self.__elems:
            raise RepositoryException("Inexistent element!!")
        idx = self.__elems.index(elem)
        self.__elems[idx] = elem

    def find(self, elem: object) -> object:
        if elem not in self.__elems:
            raise RepositoryException("Inexistent element!!")
        idx = self.__elems.index(elem)
        return self.__elems[idx]

    #def findById(self, id):

    def size(self):
        return len(self.__elems)

    def getAll(self):
        return self.__elems[:]
