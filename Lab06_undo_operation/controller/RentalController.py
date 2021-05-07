from domain import Rental, Client, Book
from controller.undoController import FunctionCall, Operation, CascadedOperation
from datetime import date
import random


class RentalController:
    '''
    Controller for rental operations
    '''

    def __init__(self, undoController, rentalRepo, bookRepo, clientRepo):
        self._books = bookRepo
        self._rentals = rentalRepo
        self._clients = clientRepo

        self._undoController = undoController

    def rent_book(self, book_id, client_id, recordUndo = True):
        '''
        rents a book
        params:
            book_id - (type str) the book id
            client - (type str) the client id
        '''
        book = self._books.find(book_id)
        client = self._clients.find(client_id)
        rental = Rental(book, client) 
        self._rentals.add(rental)

        if recordUndo == True:
            redo = FunctionCall(self.rent_book, book_id, client_id)
            undo = FunctionCall(self.delete_rental, rental.id)
            cascadeOp = CascadedOperation(Operation(undo, redo))
            self._undoController.recordOperation(cascadeOp)
        
        return rental



    def delete_rental(self, rental_id, recordUndo = True):
        rental = self._rentals.find(rental_id)

        self._rentals.delete(rental_id)


        if recordUndo == True:
            redo = FunctionCall(self.delete_rental, rental_id)
            undo = FunctionCall(self.rent_book, rental.book_id, rental.client_id)
            cascadeOp = CascadedOperation(Operation(undo, redo))
            self._undoController.recordOperation(cascadeOp)
        return rental

    def filterRentals(self, client, book):
        """
        Return a list of rentals performed by the provided client for the provided book
        params:
            client - The client performing the rental. None means all clients
            book - The rented book. None means all cars 
        """
        result = []
        for rental in self._rentals._repo:
            if (client == None or rental.client_id == client.id) and (book == None or rental.book_id == book.id):
                result.append(rental)
        return result

    def return_book(self, rental_id, year, month, day):
        '''
        adds a returned date to the rental (and so completing the renting process)
        params:
            rental_id - (type int) the id of the rental
            year, month, day - (type int)
        '''
        d = date(year, month, day)
        self._rentals.return_book(rental_id, d)

    def list_rentals(self):
        for i in self._rentals._repo:
            print(i)

#########   STATISTICS  #########
    def books_statistic(self):
        '''
        Most rented books. This will provide the list of books, sorted in descending order of the number
        of times they were rented.
        '''
        books = []
        for b in self._rentals._repo:
            books.append(b.book_id)
        books_stat = {b:books.count(b) for b in books}

        sorted_books = sorted(books_stat.items(), key=lambda x: x[1], reverse=True) ####### ask lab 9
        sorted_books_dict = {}  # we will create a dict descended with the values from book_stat  
        for i in sorted_books:
            key = i[0]
            val = i[1] 
            sorted_books_dict[key] = val
        #sorted_books_dict has (sorted) the key being the id of a book and the value the number of times it was rented
        ###### shoud the funcion return smth or just print(did not understand exactly the requirement)
        for key, value in sorted_books_dict.items():
            print(self._books.find(key).title + ' (' + str(value) + ')')

    def time_diference(self, d1, d2):
        '''
        returns the time difference btw two date objects (d1-d2)
        params:
            d1 - type data
            d2 - type data

        '''
        elapsed_time = d1 - d2
        elapsed_time = elapsed_time.days
        return elapsed_time 

    def client_statistic(self):
        '''
        Most active clients. This will provide the list of clients, sorted in descending order of the number
        of book rental days they have (e.g. having 2 rented books for 3 days each counts as 2 x 3 = 6
        days).
        '''
        clients = {}
        for b in self._rentals._repo:
            # initialises the dict
            clients[b.client_id] = 0

        for b in self._rentals._repo:
            if b._returned_date != 0:
                if self.time_diference(b._rented_date,b._returned_date) == 0:
                    clients[b.client_id] += 1
                else:
                    clients[b.client_id] += self.time_diference(b._returned_date, b._rented_date,)
            else:
                clients[b.client_id] += 1

        sorted_clients = sorted(clients.items(), key=lambda x: x[1], reverse=True) 
        
        sorted_clients_dict = {}  # we will create a dict descended with the values clients  
        for i in sorted_clients:
            key = i[0]
            val = i[1] 
            sorted_clients_dict[key] = val
        #sorted_clients_dict has (sorted) the key being the id of a book and the value the number of times it was rented
        return sorted_clients_dict   

    def author_statistic(self):
        '''
        Most rented author. This provides the list of book authored, sorted in descending order of the
        number of rentals their books have. ?
        '''
        authors = {}
        for b in self._rentals._repo:
            # initialises the dict
            authors[self._books.find(b.book_id).author] = 0

        for b in self._rentals._repo:
            authors[self._books.find(b.book_id).author] += 1

        sorted_authors = sorted(authors.items(), key=lambda x: x[1], reverse=True) 
        return sorted_authors

    def day_statistic(self, year, month, day):
        books = {}
        dat = date(year, month, day)
        for i in self._rentals._repo:
            books[self._books.find(i.book_id)] = 0
        
        for i in self._rentals._repo:
            if i.rented_date == dat:
                books[self._books.find(i.book_id)] += 1

        sorted_books = sorted(books.items(), key=lambda x: x[1])
        return sorted_books