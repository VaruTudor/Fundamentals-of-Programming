from controller.undoController import UndoController
from controller.RentalController import RentalController
from controller.ClientController import ClientController
from controller.BookController import BookController
from datetime import date
from util import printReposWithMessage
from Repository import ClientRepository, BookRepository, RentalsRepository

def undoExampleHardest():
    """
    An example for doing multiple undo operations. 
    This is a bit more difficult than in Lab2-4 due to the fact that there are now several controllers, 
    and each of them can perform operations that require undo support.
     
    Follow the code below and figure out how it works!
    """
    undoController = UndoController()
    clientRepo = ClientRepository()
    bookRepo = BookRepository()

    '''
    Start rental Controller
    '''
    rentRepo = RentalsRepository()
    rentController = RentalController(undoController, rentRepo, bookRepo, clientRepo)

    '''
    Start client Controller
    '''
    clientController = ClientController(undoController, rentController, clientRepo)

    '''
    Start book Controller
    '''
    bookController = BookController(undoController, rentController, bookRepo)

    '''
    we add 1 client, 1 book and 2 rentals
    '''

    clientSophia = clientController.add_client(103, "Sophia")
    book1 = bookController.add_book(201,'aa', 'bb')
    rentController.rent_book(201, 103)
    rentController.rent_book(201, 103)

    printReposWithMessage("We added Sophia, aa and 2 rentals", clientRepo, bookRepo, rentRepo)

    bookController.remove_book(201)

    printReposWithMessage("Delete aa (also deletes its rentals)", clientRepo, bookRepo, rentRepo)

    '''
    Now undo the performed operations, one by one
    '''
    undoController.undo()
    printReposWithMessage("1 undo, the Hyundai and its rentals are back", clientRepo, bookRepo, rentRepo)

undoExampleHardest()