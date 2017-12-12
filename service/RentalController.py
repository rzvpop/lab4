from datetime import date, timedelta

from copy import deepcopy

from domain.book import Book
from domain.client import Client
from domain.exceptions import LibraryException
from domain.rental import Rental
from service.Controller import ItemController
from service.UndoController import FunctionCall, Operation

class RentalController(ItemController):
    def __init__(self, repo, book_repo, client_repo, undo_ctrl):
        ItemController.__init__(self, repo, undo_ctrl)
        self.__book_repo = book_repo
        self.__client_repo = client_repo
        self.__undo_ctrl = undo_ctrl

    def avlBook(self, book_id):
        rentals = self._repo.getAll()
        for x in rentals:
            if x.bookId == book_id:
                state = x.rentState()
                if state["ret"] == False:
                    return False
        return True

    def addRental(self, args):
        if self.avlBook(int(args[1])):
            b = Book(int(args[1]), "default", "default", "default")
            try:
                self.__book_repo.find(b)
            except LibraryException:
                raise LibraryException("Inexistent book!")

            c = Client(int(args[2]), "default")
            try:
                self.__client_repo.find(c)
            except LibraryException:
                raise LibraryException("Unregistred client!")

            r = Rental(int(args[0]), int(args[1]), int(args[2]), date.today(), date.today() + timedelta(days=10), False)
            self._validator.rentalValidator(r)
            self._repo.add(r)
        else:
            raise LibraryException("This book is not available!")

    def getRentals(self):
        return self._repo.getAll()

    def updateRental(self, args, recForUndo = True):
        r = Rental(int(args[0]), int(args[1]), int(args[2]), args[3], args[4], args[5])
        self._validator.rentalValidator(r)
        self._repo.upd(r)

    def returnBook(self, args, recForUndo = True):
        r = Rental(int(args[0]), 1, 1, date.today(), date.today(), False)
        r = self._repo.find(r)
        old_r = deepcopy(self._repo.find(r))
        self._validator.rentalValidator(r)
        r.retDate = date.today()
        self._repo.upd(r)

        if recForUndo == True:
            undo = FunctionCall(self.updateRental, [old_r.id, old_r.bookId, old_r.clientId, old_r.renDate, old_r.dueDate, old_r.retDate], False)
            redo = FunctionCall(self.updateRental, [r.id, r.bookId, r.clientId, r.renDate, r.dueDate, r.retDate], False)
            operation = Operation(redo, undo)
            self._undo_ctrl.recordOp(operation)
