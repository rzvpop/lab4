from domain.book import Book
from domain.client import Client
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

def initClients():
    client_repo.add(Client(1, "George Ivan"))
    client_repo.add(Client(4, 'Pop Catalin'))
    client_repo.add(Client(3, "Adelin Burcasescu"))

initBooks()
initClients()

ctrl = Controller(book_repo, client_repo, rental_repo)
cons = Console(ctrl)
cons.run()