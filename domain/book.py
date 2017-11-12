class Book:
    def __init__(self, id = 0, title = "", desc = "", author = ""):
        self.__id = id
        self.__title = title
        self.__desc = desc
        self.__author = author

    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, value):
        self.__id = value

    @property
    def title(self):
        return self.__title

    @title.setter
    def title(self, value):
        self.__title = value

    @property
    def desc(self):
        return self.__desc

    @desc.setter
    def desc(self, value):
        self.__desc = value

    @property
    def author(self):
        return self.__author

    @author.setter
    def author(self, value):
        self.__author = value

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self.__id == other.__id
        else:
            return False

    def __str__(self):
        return "#" + str(self.__id) + " Title: '" + self.__title + "' | " + "Author: " + self.__author + " | "\
               + "Description: " + self.__desc
