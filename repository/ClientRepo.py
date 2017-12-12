from domain.client import Client
from repository.Repository import Repository, RepositoryException


class ClientFileRepository(Repository):
    def __init__(self, f_name="clients.txt"):
        Repository.__init__(self)
        self.__f_name = f_name
        self.__loadFromFile()

    def add(self, client):
        Repository.add(self, client)
        self.__storeToFile()

    def rem(self, client):
        Repository.rem(self, client)
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
                c = Client(int(attrs[0]), attrs[1])
                Repository.add(self, c)
                line = f.readline().strip()
        except IOError:
            raise RepositoryException("Can't load data from file " + self.__f_name + "!")
        f.close()

    def __storeToFile(self):
        f = open(self.__f_name, "w")
        clients = Repository.getAll(self)

        for client in clients:
            str_client = str(client.id) + ", " + client.name + "\n"
            f.write(str_client)

        f.close()