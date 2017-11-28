from datetime import date, timedelta
from domain.book import Book
from domain.client import Client
from domain.rental import Rental
from service.BookController import BookController
from service.ClientController import ClientController
from service.RentalController import RentalController
from ui.Console import Console
from repository.Repository import Repository

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

def initRentals():
    ren_d = date.today()
    due_d = ren_d + timedelta(days=10)

    rental_repo.add(Rental(1, 1, 4, ren_d, due_d, False))
    rental_repo.add(Rental(2, 5, 3, ren_d, due_d, False))


initBooks()
initClients()
initRentals()

b_ctrl = BookController(book_repo)
c_ctrl = ClientController(client_repo)
r_ctrl = RentalController(rental_repo, book_repo, client_repo)
cons = Console(b_ctrl, c_ctrl, r_ctrl)
cons.run()