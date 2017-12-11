from datetime import date, timedelta
from domain.book import Book
from domain.client import Client
from domain.rental import Rental
from service.BookController import BookController
from service.ClientController import ClientController
from service.RentalController import RentalController
from service.StatisticsController import StatisticsController
from service.UndoController import UndoController
from ui.Console import Console
from repository.Repository import Repository

book_repo = Repository()
client_repo = Repository()
rental_repo = Repository()
op_list = []

def initBooks():
    book_repo.add(Book(2, "Infernul", "plm", "Dante"))
    book_repo.add(Book(1, "Poezii", "misto", "Eminescu"))
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

undo_ctrl = UndoController(op_list)
b_ctrl = BookController(book_repo, undo_ctrl)
c_ctrl = ClientController(client_repo, undo_ctrl)
r_ctrl = RentalController(rental_repo, book_repo, client_repo, undo_ctrl)
s_ctrl = StatisticsController(book_repo, client_repo, rental_repo, undo_ctrl)

cons = Console(b_ctrl, c_ctrl, r_ctrl, s_ctrl, undo_ctrl)
cons.run()