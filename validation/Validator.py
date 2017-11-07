class ValidationExcention(Exception):
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
            raise ValidationExcention(errors)
