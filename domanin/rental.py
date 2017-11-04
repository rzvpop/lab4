class Rental:
    def __init__(self, id, book_id, client_id, ren_date, due_date, ret_date):
        self._id = id
        self._book_id = book_id
        self._client_id = client_id
        self._ren_date = ren_date
        self._due_date = due_date
        self.ret_date = ret_date

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value):
        self._id = value

    @property
    def bookId(self):
        return self._book_id

    @bookId.setter
    def bookId(self, value):
        self._book_id = value

    @property
    def clientId(self):
        return self._client_id

    @clientId.setter
    def clientId(self, value):
        self._client_id = value

    @property
    def renDate(self):
        return self._ren_date

    @renDate.setter
    def renDate(self, value):
        self._ren_date = value

    @property
    def dueDate(self):
        return self._due_date

    @dueDate.setter
    def dueDate(self, value):
        self._due_date = value

    @property
    def retDate(self):
        return self._ret_date

    @retDate.setter
    def retDate(self, value):
        self._ret_date = value

    #schimb id cu numele
    def __str__(self):
        return "#" + str(self._id) + " | Book: " + str(self._client_id) + " | Client: " + str(self._client_id) + "\n"\
                "| Rental date:" + self._ren_date + " | Due date: " + self._due_date + " | Returned on: " + self._ret_date