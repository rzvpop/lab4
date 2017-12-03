import re

from domain.exceptions import LibraryException


class Console:
    def __init__(self, b_ctrl, c_ctrl, r_ctrl, s_ctrl):
        self.__b_ctrl = b_ctrl
        self.__c_ctrl = c_ctrl
        self.__r_ctrl = r_ctrl
        self.__s_ctrl = s_ctrl

    def exitApp(self):
        exit(0)

    def help(self):
        cmd_str = "Commands:\n"

        cmd_str += "- exit\n"
        cmd_str += "- help\n"
        cmd_str += "- add book\n"
        cmd_str += "- list books\n"
        cmd_str += "- remove book\n"
        cmd_str += "- update book\n"
        cmd_str += "- add client\n"
        cmd_str += "- list clients\n"
        cmd_str += "- remove client\n"
        cmd_str += "- update client\n"
        cmd_str += "- rent book\n"
        cmd_str += "- list rentals\n"
        cmd_str += "- return book\n"

        print(cmd_str)

    def addBook(self):
        id = input("Id: ")
        title = input("Title: ")
        desc = input("Descrpition: ")
        author = input("Author: ")
        args = [id, title, desc, author]

        self.__b_ctrl.addBook(args)
        print("Book added!")

    def listBooks(self):
        books = self.__b_ctrl.getItems()

        if len(books) == 0:
            print("No books!")
            return
        for x in books:
            print(x, '\n')

    def removeBook(self, args):
        self.__b_ctrl.removeBook(int(args[0]))
        print("Book removed!")

    def updateBook(self, args):
        self.__b_ctrl.updateBook(args)
        print("Book updated!")

    def addClient(self):
        id = input("Id: ")
        name = input("Name: ")
        args = [id, name]

        self.__c_ctrl.addClient(args)
        print("Client added!")

    def listClients(self):
        clients = self.__c_ctrl.getItems()

        if len(clients) == 0:
            print("No clients!")
            return
        for x in clients:
            print(x, '\n')

    def removeClient(self, args):
        self.__c_ctrl.removeClient(args[0])
        print("Client removed!")

    def updateClient(self, args):
        self.__c_ctrl.updateClient(args)
        print("Client updated!")

    def addRental(self):
        id = input("Id: ")
        b_id = input("Book id: ")
        c_id = input("Client id: ")
        args = [id, b_id, c_id]

        self.__r_ctrl.addRental(args)
        print("Book rented!")

    def listRentals(self):
        rentals = self.__r_ctrl.getItems()

        if len(rentals) == 0:
            print("No clients!")
            return
        for x in rentals:
            print(x, '\n')

    def returnBook(self, args):
        self.__r_ctrl.returnBook(args)
        print("Book returned!")

    def bookSearch(self):
        hint = input("Hint: ")
        hint = hint.lower()
        l = self.__s_ctrl.bookSearch(hint)

        for x in l:
            print(x, '\n')

    def clientSearch(self):
        hint = input("Hint: ")
        hint = hint.lower()
        l = self.__s_ctrl.clientSearch(hint)

        for x in l:
            print(x, '\n')

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
            "update_client": r"^\s*update\s*client\s*([0-9\s]+)\s*,\s*([a-zA-Z0-9\s]+)\s*$",
            "add_rental": r"^\s*rent\s*book\s*$",
            "list_rentals": r"^\s*list\s*rentals\s*$",
            "return_book": r"^\s*return\s*([0-9]+)\s*$",
            "search_book": r"^\s*search\s*book\s*$",
            "search_client": r"^\s*search\s*client\s*$",
            "help": r"^\s*help\s*",
            "exit": r"^\s*exit\s*$"
        }
        return d

    def cmdList(self):
        l = [["exit", self.exitApp, False],
             ["help", self.help, False],
             ["add_book", self.addBook, True],
             ["list_books", self.listBooks, False],
             ["remove_book", self.removeBook, True],
             ["update_book", self.updateBook, True],
             ["add_client", self.addClient, True],
             ["list_clients", self.listClients],
             ["remove_client", self.removeClient, True],
             ["update_client", self.updateClient, True],
             ["add_rental", self.addRental, True],
             ["list_rentals", self.listRentals, False],
             ["return_book", self.returnBook, True],
             ["search_book", self.bookSearch, False],
             ["search_client", self.clientSearch, False]
        ]
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
                                except LibraryException as ex:
                                    print(ex)
                            else:
                                try:
                                    i[1]()
                                except LibraryException as ex:
                                    print(ex)
            if not found:
                print("Invalid command syntax!")