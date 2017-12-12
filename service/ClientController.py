from copy import deepcopy

from domain.client import Client
from service.Controller import ItemController
from service.UndoController import FunctionCall, Operation

class ClientController(ItemController):
    def addClient(self, args, recForUndo = True):
        c = Client(int(args[0]), args[1])
        self._validator.validateClient(c)
        self._repo.add(c)

        if recForUndo == True:
            undo = FunctionCall(self.removeClient, c.id, False)
            redo = FunctionCall(self.addClient, [c.id, c.name], False)
            operation = Operation(redo, undo)
            self._undo_ctrl.recordOp(operation)

    def removeClient(self, id, recForUndo = True):
        c = Client(int(id), "default")
        self._validator.validateClient(c)
        self._repo.rem(c)

        if recForUndo == True:
            undo = FunctionCall(self.addClient, [c.id, c.name], False)
            redo = FunctionCall(self.removeClient, c.id, False)
            operation = Operation(redo, undo)
            self._undo_ctrl.recordOp(operation)

    def updateClient(self, args, recForUndo = True):
        c = Client(int(args[0]), args[1])
        self._validator.validateClient(c)
        old_c = deepcopy(self._repo.find(c))
        self._repo.upd(c)

        if recForUndo == True:
            undo = FunctionCall(self.updateClient, [old_c.id, old_c.name], False)
            redo = FunctionCall(self.updateClient, [c.id, c.name], False)
            operation = Operation(redo, undo)
            self._undo_ctrl.recordOp(operation)