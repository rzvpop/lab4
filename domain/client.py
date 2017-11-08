class Client:
    def __init__(self, id, name):
        self.__id = id
        self.__name = name

    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, value):
        self.__id = value

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value

    def __eq__(self, other):
        if isinstance(other,self.__class__):
            return self.__id == other.__id
        else:
            return False

    def __str__(self):
        return "#" + str(self.__id) + " Nume: " + self.__name
