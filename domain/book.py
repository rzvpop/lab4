class Book:
    def __init__(self, id = 0, title = "", desc = "", author = ""):
        self._id = id
        self._title = title
        self._desc = desc
        self._author = author

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value):
        self._id = value

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        self._title = value

    @property
    def desc(self):
        return self._desc

    @desc.setter
    def desc(self, value):
        self._desc = value

    @property
    def author(self):
        return self._author

    @author.setter
    def author(self, value):
        self._author = value

    def __eq__(self, b):
        return self._id == b.id

    def __str__(self):
        return "#" + str(self._id) + " Title: '" + self._title + "' | " + "Author: " + self._author + " | "\
               + "Description: " + self._desc


def testBook():
    b = Book(3, "10 big niggers", "detective Fictionwad", "agatha Cristie")

    assert(isinstance(b, Book))

    assert(b.id == 3)
    assert(b.title == "10 big niggers")
    assert(b.author == "agatha Cristie")
    assert(b.desc == "detective Fictionwad")

    b._id = 1
    b.title = "10 little niggers"
    b.author = "Agatha Cristie"
    b.desc = "detective fiction"

    assert(b.id == 1)
    assert(b.title == "10 little niggers")
    assert(b.author == "Agatha Cristie")
    assert(b.desc == "detective fiction")

    assert(b.__str__() == "#1 Title: '10 little niggers' | Author: Agatha Cristie | Description: detective fiction")

testBook()