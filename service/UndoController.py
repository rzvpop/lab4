class UndoController():
    def __init__(self, op_list):
        self.__op_list = op_list
        self.__index = -1

    def recordOp(self, operation):

        self.__op_list = self.__op_list[:(self.__index + 1)]
        self.__op_list.append(operation)
        self.__index += 1

    def undo(self):
        if self.__index != -1:
            self.__op_list[self.__index].undo()
            self.__index -= 1
            return True
        return False

    def redo(self):
        if self.__index != len(self.__op_list) - 1:
            self.__index += 1
            self.__op_list[self.__index].redo()
            return True
        return False

class FunctionCall:
    def __init__(self, functionRef, *parameters):
        self._functionRef = functionRef
        self._parameters = parameters

    def call(self):
        self._functionRef(*self._parameters)


class Operation:
    def __init__(self, functionDo, functionUndo):
        self._functionDo = functionDo
        self._functionUndo = functionUndo

    def undo(self):
        self._functionUndo.call()

    def redo(self):
        self._functionDo.call()