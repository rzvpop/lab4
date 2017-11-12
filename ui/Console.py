import re

from domain.exceptions import LibraryException


class Console:

    def __init__(self, ctrl):
        self.__ctrl = ctrl

    def exitApp(self):
        exit(0)

    def addBook(self):
        id = input("Id: ")
        title = input("Title: ")
        desc = input("Descrpition: ")
        author = input("Author: ")
        args = [id, title, desc, author]

        self.__ctrl.addBook(args)
        print("Book added!")

    def listBooks(self):
        books = self.__ctrl.getBooks()

        if len(books) == 0:
            print("No books!")
            return
        for x in books:
            print(x, '\n')

    def removeBook(self, args):
        self.__ctrl.removeBook(int(args[0]))
        print("Book removed!")

    def updateBook(self, args):
        self.__ctrl.updateBook(args)
        print("Book updated!")

    def addClient(self):
        id = input("Id: ")
        name = input("Name: ")
        args = [id, name]

        self.__ctrl.addClient(args)
        print("Client added!")

    def listClients(self):
        clients = self.__ctrl.getClients()

        if len(clients) == 0:
            print("No clients!")
            return
        for x in clients:
            print(x, '\n')

    def removeClient(self, args):
        self.__ctrl.removeClient(args[0])
        print("Client removed!")

    def updateClient(self, args):
        self.__ctrl.updateClient(args)
        print("Client updated!")

    def syntaxDict(self):
        d = {
            "add_book": r"^\s*add\s*book\s*$",
            "list_books": r"^\s*list\s*books\s*$",
            "remove_book": r"^\s*remove\s*book\s*([0-9]+)\s*$",
            "update_book": r"^\s*update\s*book\s*"
                           r"([0-9\s]+)\s*,\s*([a-zA-Z0-9\s]+)\s*,\s*([a-zA-Z0-9\s]+)\s*,\s*([a-zA-Z0-9\s]+)\s*$",
            "add_client": r"^\s*add\s*client\s*$",
            "list_clients": r"^\s*list\s*clients\s*$",
            "remove_client": r"^\s*remove\s*client\s*([0-9]+)\s*$",
            "update_client": r"^\s*update\s*client\s*([0-9\s]+)\s*,\s*([a-zA-Z0-9\s]+)\s*",
            "exit": r"^\s*exit\s*$"
        }
        return d

    def cmdList(self):
        l = [["exit", self.exitApp, False],
             ["add_book", self.addBook, True],
             ["list_books", self.listBooks, False],
             ["remove_book", self.removeBook, True],
             ["update_book", self.updateBook, True],
             ["add_client", self.addClient, True],
             ["list_clients", self.listClients],
             ["remove_client", self.removeClient, True],
             ["update_client", self.updateClient, True]]
        return l

    def run(self):
        actions = self.cmdList()
        syntax_dict = self.syntaxDict()

        while True:
            user_input = input('>>')
            found = False

            for x, y in syntax_dict.items():
                matches = re.match(y, user_input)

                if matches:
                    found = True

                    for i in actions:
                        if x == i[0]:
                            if len(matches.groups()) >= 1:
                                try:
                                    i[1](matches.groups())
                                except Exception as ex:
                                    print(ex)
                            else:
                                try:
                                    i[1]()
                                except Exception as ex:
                                    print(ex)
            if not found:
                print("Invalid command syntax!")