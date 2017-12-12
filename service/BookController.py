from copy import deepcopy

from domain.book import Book
from service.Controller import ItemController
from service.UndoController import FunctionCall, Operation


class BookController(ItemController):
    def addBook(self, args, recForUndo = True):
        b = Book(int(args[0]), args[1], args[2], args[3])
        self._validator.validateBook(b)
        self._repo.add(b)

        if recForUndo == True:
            undo = FunctionCall(self.removeBook, b.id, False)
            redo = FunctionCall(self.addBook, [b.id, b.title, b.desc, b.author], False)
            operation = Operation(redo, undo)
            self._undo_ctrl.recordOp(operation)

    def removeBook(self, id, recForUndo = True):
        b = Book(int(id), "default", "default", "default")
        self._validator.validateBook(b)
        b = self._repo.rem(b)

        if recForUndo == True:
            undo = FunctionCall(self.addBook, [b.id, b.title, b.desc, b.author], False)
            redo = FunctionCall(self.removeBook, b.id, False)
            operation = Operation(redo, undo)
            self._undo_ctrl.recordOp(operation)

    def updateBook(self, args, recForUndo = True):
        b = Book(int(args[0]), args[1], args[2], args[3])
        self._validator.validateBook(b)
        old_b = deepcopy(self._repo.find(b))
        self._repo.upd(b)

        if recForUndo == True:
            undo = FunctionCall(self.updateBook, [old_b.id, old_b.title, old_b.desc, old_b.author], False)
            redo = FunctionCall(self.updateBook, [b.id, b.title, b.desc, b.author], False)
            operation = Operation(redo, undo)
            self._undo_ctrl.recordOp(operation)
