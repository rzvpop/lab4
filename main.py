from datetime import date, timedelta
from domain.book import Book
from domain.client import Client
from domain.rental import Rental
from repository.BookRepo import BookFileRepository
from repository.ClientRepo import ClientFileRepository
from repository.RentalRepo import RentalFileRepository
from service.BookController import BookController
from service.ClientController import ClientController
from service.RentalController import RentalController
from service.StatisticsController import StatisticsController
from service.UndoController import UndoController
from ui.Console import Console
from repository.Repository import Repository

book_repo = BookFileRepository()
client_repo = ClientFileRepository()
rental_repo = RentalFileRepository()
op_list = []

undo_ctrl = UndoController(op_list)
b_ctrl = BookController(book_repo, undo_ctrl)
c_ctrl = ClientController(client_repo, undo_ctrl)
r_ctrl = RentalController(rental_repo, book_repo, client_repo, undo_ctrl)
s_ctrl = StatisticsController(book_repo, client_repo, rental_repo)

cons = Console(b_ctrl, c_ctrl, r_ctrl, s_ctrl, undo_ctrl)
cons.run()