'''
UI
'''
from controller.undoController import UndoController
from Repository import ClientRepository, BookRepository, RentalsRepository
from controller.BookController import BookController
from controller.ClientController import ClientController
from controller.RentalController import RentalController
from domain import Book, Client, Rental
import random
from exceptions import BadIDError
from datetime import date

class PrindMenus:
    def print_menu(self):
        print ('1. Manage the list of persons and activities')
        print ('2. Add/remove activities')
        print ('3. Search')
        print ('4. Statistics')
        print ('5. exit')
        print ('6. undo')
        print ('7. redo')

    def print_1(self):
        print('1. add book')
        print('2. remove book')
        print('3. show books')
        print('4. update book')
        print('5. add client')
        print('6. remove client')
        print('7. show clients')
        print('8. update client')
        print('9. add client_2')

    def print_2(self):
        print('1. rent a book')
        print('2. return a book')
        print('3. list all rentals')

    def print_3(self):
        print ('1. Search book by id')
        print ('2. Search book by title')
        print ('3. Search book by author')
        print ('4. Search client by id')
        print ('5. Search client by name')

    def print_4(self):
        print('1. Book statistic')
        print('2. Client statistic')
        print('3. Author statistic')
        print('4. lab 8 statistic')



class UI(PrindMenus):
    def __init__(self, bookController, clientController, rentalController, undoController):
        self._bookController = bookController
        self._clientController = clientController
        self._rentalController = rentalController
        self._undoController = undoController

    def add_book_ui(self):
        title = input ('title: ')
        author = input ('author: ')
        book_id = int(random.choice(range(1000, 9999)))
        try:
            self._bookController.add_book(book_id, title, author)
        except BadIDError:
            print ('there is another book with the same id')
    
    def remove_book_ui(self):
        book_id = int(input ('give book id: '))
        self._bookController.remove_book(book_id)

    def update_book_ui(self):
        old_id = input('book id: ')
        new_title = input('title to update: ')
        new_author = input('author to update: ')
        self._bookController.update_book(old_id, new_title, new_author)

    def add_client_ui(self):
        name = input ('name: ')
        id_1 = int(random.choice(range(1000 , 9999)))
        try:
            self._clientController.add_client(id_1, name)
        except BadIDError:
            print ('There alrready exists a client with the same id')

    def add_client_ui_2(self):
        #lab requirement
        name = input ('name: ')
        id_1 = int(random.choice(range(1000 , 9999)))
        try:
            self._clientController.add_client_2(id_1, name)
        except ValueError:
            print ('There alrready exists a client with the same id')

    def remove_client_ui(self):
        client_id = input('id: ')
        self._clientController.remove_client(client_id)        

    def update_client_ui(self):
        client_id = input('client id: ')
        new_name = input('name to update: ')
        self._clientController.update_client(client_id, new_name)

    def rent_book_ui(self):
        book_id = input('give book id: ')
        client_id = input('give client id: ')
        self._rentalController.rent_book(book_id, client_id)

    def return_ui(self):
        rent_id = input('give rental id: ')
        year = int(input('give year: '))
        month = int(input('give month: '))
        day = int(input('give day: '))
        self._rentalController.return_book(rent_id, year, month, day)

    def search_client_id_ui(self):
        client_id = int(input('give client id: '))
        self._clientController.search_client_id(client_id)

    def search_client_name_ui(self):
        name = input('give client name: ')
        self._clientController.search_client_name(name)

    def search_book_id_ui(self):
        book_id = int(input('give book id: '))
        self._bookController.search_book_id(book_id)

    def search_book_title_ui(self):
        title = input('give book title: ')
        self._bookController.search_book_title(title)

    def search_book_author_ui(self):
        author = input('give book author: ')
        self._bookController.search_book_author(author)
    
####### STATISTICS UI START #######

    def client_statistic_ui(self):
        clients = self._rentalController.client_statistic()
        for key, value in clients.items():
            print(self._rentalController._clients.find(key).name + ' (' + str(value) + ' days)')

    def date_statistic_ui(self):
        year = int(input('give year: '))
        month = int(input('give month: '))
        day = int(input('give day: '))
        books = self._rentalController.day_statistic(year, month, day)
        for b in books:
            book = b[0]
            times = b[1]
            print (book.title + ' times rented ' + str(times))

    def author_statistic_ui(self):
        authors = self._rentalController.author_statistic()
        for a in authors:
            print(a[0] + ' has ' + str(a[1]) + ' books rented')

####### STATISTICS UI END #######

################### DELETE OCCURENCES OF STRING IN THE OUTPUT ###################
    def delete_string_from_output_ui(self):
        stringToDelete = input("Enter string that you want to be deleted: ")
        self._clientController.list_clients(stringToDelete)
#############################################

    def start(self):
        # self._rentalController.initialize_rentals()
        while True:
            self.print_menu()
            command = input ('enter command: ')
            if command == '1':
                self.print_1()
                command_1 = input ('what do u want to do: ')
                if command_1 == '1': 
                    self.add_book_ui()
                elif command_1 == '2':
                    self.remove_book_ui()
                elif command_1 == '3':
                    self._bookController.list_books()
                elif command_1 == '4': 
                    self.update_book_ui()
                elif command_1 == '5': 
                    self.add_client_ui()
                elif command_1 == '6': 
                    self.remove_client_ui()
                elif command_1 == '7': 
                    self._clientController.list_clients()
                elif command_1 == '8': 
                    self.update_client_ui()
                elif command_1 == '9':
                    self.add_client_ui_2()
                else:
                    print ('Wrong Command')
            elif command == '2':
                self.print_2()
                command_2 = input('what do u want to do: ')
                if command_2 == '1':
                    self.rent_book_ui()
                elif command_2 == '2':
                    self.return_ui()
                elif command_2 == '3':
                    self._rentalController.list_rentals()
                else:
                    print ('Wrong Command')                    
            elif command == '3':
                self.print_3()
                command_3 = input('what do u want to do: ')
                if command_3 == '1':
                    self.search_book_id_ui()
                elif command_3 == '2':
                    self.search_book_title_ui()
                elif command_3 == '3':
                    self.search_book_author_ui()
                elif command_3 == '4':
                    self.search_client_id_ui()
                elif command_3 == '5':
                    self.search_client_name_ui()
                else:
                    print('wrong command')
            elif command == '4':
                self.print_4()
                command_4 = input('choose: ')
                if command_4 == '1':
                    self._rentalController.books_statistic()
                elif command_4 == '2':
                    self.client_statistic_ui()
                elif command_4 == '3':
                    self.author_statistic_ui()
                elif command_4 == '4':
                    self.date_statistic_ui()
                else:
                    print('wrong command')
            elif command == '5':
                return
            elif command == '6':
                try:
                    self._undoController.undo()
                except ValueError as v:
                    print(v)
            elif command == '7':
                try:
                    self._undoController.redo()
                except ValueError as v:
                    print(v)
            elif command == '8':
                # enter a string and delete every occurence in the output
                self.delete_string_from_output_ui()
            else :
                print ('wrong command')