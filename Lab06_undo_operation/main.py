from controller.BookController import BookController
from controller.ClientController import ClientController
from controller.RentalController import RentalController
from controller.undoController import UndoController
from UI import UI
from Repository import ClientRepository, BookRepository, RentalsRepository
from domain import Book
from configparser import ConfigParser

undo_controller = UndoController()


### normal ui ###
clients = ClientRepository()
books = BookRepository()
rentals = RentalsRepository(books, clients)
### create controllers ###
rentalController = RentalController(undo_controller, rentals, books, clients)
bookController = BookController(undo_controller, rentalController, books)
clientController = ClientController(undo_controller, rentalController, clients)
### create ui ###
ui = UI(bookController, clientController, rentalController, undo_controller)
ui.start()