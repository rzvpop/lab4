from datetime import date


class ValidationException(Exception):
    pass


class Validator():
    def validateBook(self, book):
        errors = ""

        if book.id < 0:
            errors += "Invalid id!\n"
        if book.title == "":
            errors += "Invalid title!\n"
        if book.desc == "":
            errors += "Invalid description!\n"
        if book.author == "":
            errors += "Invalid author!\n"

        if len(errors) > 0:
            raise ValidationException(errors)

    def validateClient(self, client):
        errors = ""

        if client.id < 0:
            errors += "Invalid id!\n"
        if client.name == "":
            errors += "Invalid name!\n"

        if len(errors) > 0:
            raise ValidationException(errors)

    def rentalValidator(self, rental):
        errors = ""

        if rental.id < 0:
            errors += "Invalid id!\n"
        if rental.bookId < 0:
            errors += "Invalid book id!\n"
        if rental.clientId < 0:
            errors += "Invalid client id!\n"
        if not isinstance(rental.renDate, date):
            errors += "Invalid rent date!\n"
        if not isinstance(rental.dueDate, date):
            errors += "Invalid due date!\n"
        if not (isinstance(rental.retDate, date) or isinstance(rental.retDate, bool)):
            errors += "Invalid return date!\n"

        if len(errors) > 0:
            raise ValidationException(errors)