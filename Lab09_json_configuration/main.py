from controller.BookController import BookController
from controller.ClientController import ClientController
from controller.RentalController import RentalController
from controller.undoController import UndoController
from UI import UI
from Repository import ClientRepository, BookRepository, RentalsRepository
##  text repos  ##
from textRepos.booktextrepository import BookTextRepository
from textRepos.client_text_repository import ClientTextRepository
from textRepos.rental_text_repository import RentalTextRepository
##  end text repos  ##

##  pickle repos    ##
from pickleRepos.book_pickle_repository import BookPikleRepository
from pickleRepos.client_pickle_repository import ClinetPikleRepository
from pickleRepos.rentals_pickle_repository import RentalsPikleRepository
##  end pickle repos    ##

##  JSON repos    ##
from book_json_repository import BookJsonRepository
from client_json_repository import ClientJsonRepository
from rentals_json_repository import RentalJsonRepository
##  end JSON repos    ##

##  lab ##
from booktextrepository_lab import BookTextRepositoryLab
##  end lab ##

from domain import Book
from configparser import ConfigParser

parser = ConfigParser()
parser.read('settings.properties')

print('which repo do u want')
print('text, binary, json, lab or in-app')
command = input('choose: ')

undo_controller = UndoController()

if command == parser.sections()[1]:
    ### text ui ###
    books2 = BookTextRepository('books.txt')
    clients2 = ClientTextRepository('clients.txt')
    rentals2 = RentalTextRepository('rentals.txt', books2, clients2)
    ### end text ui ###
    rentalController2 = RentalController(undo_controller, rentals2, books2, clients2)
    bookController2 = BookController(undo_controller, rentalController2, books2)
    clientController2 = ClientController(undo_controller, rentalController2, clients2)
    ui2 = UI(bookController2, clientController2, rentalController2, undo_controller)
    ui2.start()


elif command == parser.sections()[0]:
    ### pickle ui ###
    books3 = BookPikleRepository('books.pickle')
    clients3 = ClinetPikleRepository('clients.pickle')
    rentals3 = RentalsPikleRepository('rentals.pickle')
    ### end pickle ui ###
    rentalController3 = RentalController(undo_controller, rentals3, books3, clients3)
    booksController3 = BookController(undo_controller, rentalController3, books3)
    clientController3 = ClientController(undo_controller, rentalController3, clients3)
    ui3 = UI(booksController3, clientController3, rentalController3, undo_controller)
    ui3.start()


elif command == parser.sections()[2]:
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

elif command == parser.sections()[3]:
    ### json ui ###
    clients4 = ClientJsonRepository('clients.json')
    books4 = BookJsonRepository('books.json')
    rentals4 = RentalJsonRepository('rentals.json',books4, clients4)
    ### create controllers ###
    rentalController = RentalController(undo_controller, rentals4, books4, clients4)
    bookController = BookController(undo_controller, rentalController, books4)
    clientController = ClientController(undo_controller, rentalController, clients4)
    ### create ui ###
    ui = UI(bookController, clientController, rentalController, undo_controller)
    ui.start()

elif command == parser.sections()[4]:
    ### normal ui ###
    clients = ClientRepository()
    books = BookTextRepositoryLab('book2.txt','book2help.txt')
    rentals = RentalsRepository(books, clients)
    ### create controllers ###
    rentalController = RentalController(undo_controller, rentals, books, clients)
    bookController = BookController(undo_controller, rentalController, books)
    clientController = ClientController(undo_controller, rentalController, clients)
    ### create ui ###
    ui = UI(bookController, clientController, rentalController, undo_controller)
    ui.start()

else:
    print ('THAT IS NOT A GOOD COMMAND')