from domain.book import Book
from ui.Console import Console
from repository.Repository import Repository
from service.Controller import Controller

book_repo = Repository()
client_repo = Repository()
rental_repo = Repository()

def initBooks():
    book_repo.add(Book(1, "Infernul", "plm", "Dante"))
    book_repo.add(Book(2, "Poezii", "misto", "Eminescu"))
    book_repo.add(Book(5, "plt", "plm", "pln"))

initBooks()

ctrl = Controller(book_repo, client_repo, rental_repo)
cons = Console(ctrl)
cons.run()