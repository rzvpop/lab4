from datetime import date, datetime


class Rental:
    def __init__(self, id, book_id, client_id, ren_date, due_date, ret_date):
        self.__id = id
        self.__book_id = book_id
        self.__client_id = client_id
        self.__ren_date = ren_date
        self.__due_date = due_date
        self.__ret_date = ret_date

    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, value):
        self.__id = value

    @property
    def bookId(self):
        return self.__book_id

    @bookId.setter
    def bookId(self, value):
        self.__book_id = value

    @property
    def clientId(self):
        return self.__client_id

    @clientId.setter
    def clientId(self, value):
        self.__client_id = value

    @property
    def renDate(self):
        return self.__ren_date

    @renDate.setter
    def renDate(self, value):
        self.__ren_date = value

    @property
    def dueDate(self):
        return self.__due_date

    @dueDate.setter
    def dueDate(self, value):
        self.__due_date = value

    @property
    def retDate(self):
        return self.__ret_date

    @retDate.setter
    def retDate(self, value):
        self.__ret_date = value

    def rentState(self):
        state = {"ret": False, "late": False}

        if self.__ret_date != False:
            state["ret"] = True
            if date.today() > self.__due_date:
                state["late"] = True

        return state

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self.__id == other.__id
        else:
            return False

    #schimb id cu numele
    def __str__(self):
        rent_date = self.__ret_date
        if rent_date == False:
            rent_date = "-"

        return "#" + str(self.__id) + " | Book: " + str(self.__book_id) + " | Client: " + str(self.__client_id) + "\n"\
                "| Rental date: " + str(self.__ren_date) + " | Due date: " + str(self.__due_date) + " | Returned on: " + str(rent_date)
