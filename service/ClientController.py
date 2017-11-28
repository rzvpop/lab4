from domain.client import Client
from service.Controller import ItemController


class ClientController(ItemController):
    def addClient(self, args):
        c = Client(int(args[0]), args[1])
        self._validator.validateClient(c)
        self._repo.add(c)

    def removeClient(self, id):
        c = Client(int(id), "default")
        self._validator.validateClient(c)
        self._repo.rem(c)

    def updateClient(self, args):
        c = Client(int(args[0]), args[1])
        self._validator.validateClient(c)
        self._repo.upd(c)