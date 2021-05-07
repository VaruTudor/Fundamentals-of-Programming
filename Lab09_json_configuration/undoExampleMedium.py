from domain import Book, Client, Rental
from controller.RentalController import RentalController
from controller.BookController import BookController
from controller.ClientController import ClientController
from controller.undoController import UndoController
from datetime import date
from Repository import BookRepository, ClientRepository, RentalsRepository
from util import printReposWithMessage

def undoExampleMedium():
    undoController = UndoController()
    bookRepo = BookRepository()
    clientRepo = ClientRepository()

    # start rental controller
    rentRepo = RentalsRepository()
    rentController = RentalController(undoController, rentRepo, bookRepo, clientRepo)

    # start client controller
    clientController = ClientController(undoController, rentController, clientRepo)

    # start book controller
    bookController = BookController(undoController, rentController, bookRepo)

    # we add 3 clients
    clientSophia = clientController.add_client(103, "Sophia")
    clientCarol = clientController.add_client(104, "Carol")
    clientBob = clientController.add_client(105, "Bob")
    printReposWithMessage('we added 3 clients', clientRepo, None, None)

    # we delete 2 clients
    clientController.remove_client(103)
    clientController.remove_client(105)
    printReposWithMessage("Deleted Sophia and Bob", clientRepo, None, None)

    # we undo twice
    undoController.undo()
    printReposWithMessage("1 undo, so Bob is back", clientRepo, None, None)
    undoController.undo()
    printReposWithMessage("Another undo, so Sophia is back too", clientRepo, None, None)

    # we redo twice
    undoController.redo()
    printReposWithMessage("1 redo, so Sophia is again deleted", clientRepo, None, None)

undoExampleMedium()