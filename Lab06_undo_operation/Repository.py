from domain import Book, Client, Rental
from exceptions import BadIDError,NotFoundID
import random
from datetime import date


class Repository:
    def __init__(self):
        self._repo = []

    def add(self, element):
        '''
            adds an element to the repo
            params:
                element - will be added to self._repo (type list)
        '''
        self._repo.append(element)

    def find(self, element_id):
        '''
            finds and returns an element by its id
            params:
                element_id - the id of the element (type int)
            return:
                the object which coresponds to the id
        '''
        for obj in self._repo:
            if int(obj.id) == int(element_id):
                return obj

    def delete(self, element_id):
        '''
            deletes an element by its id
            params:
                element_id - the id of the element (type int)     
        '''
        self._repo.remove(self.find(element_id))

    def __str__(self):
        r = ''
        for e in self._repo:
            r += str(e)
            r += '\n'
        return r

class ClientRepository(Repository):
    def __init__(self):
        Repository.__init__(self)
        self.initialize_list()

    def initialize_list(self):
        name_options = ['andrei','alex','maria','cristi','oana','teodora','marcel','rares','alexandra']
        list_ids = range(1000,9999)
        i = 1
        while i <10:
            client_id = random.choice(list_ids)
            name = random.choice(name_options)
            client = Client(client_id, name)
            try:
                self.add(client)
                i+= 1
            except BadIDError:
                i-= 1

    def update(self, client_id, new_name):
        '''
        updates a client
        params:
            client_id - (type int)
            new_name - (type str)
        '''
        k = self.find(client_id)
        k.name = new_name


class BookRepository(Repository):
    def __init__(self):
        Repository.__init__(self)
        self.initialize_list()

    def initialize_list(self):
        book_options = [
            ['André Brink','A Dry White Season'],
            ['Nikos Kazantzakis','Zorba the Greek'],
            ['Kathleen Winter','Annabele'],
            ['Toni Morrison','Song of Solomon'],
            ['Leo Tolstoy','War and Peace'],
            ['James Joyce','Ulysses'],
            ['Carlos Ruiz Zafon','The Shadow of the Wind'],
            ['J.R.R. Tolkien','The Lord of the Rings'],
            ['Salman Rushdie','The Satanic Verses'],
            ['Don Quixote','Miguel de Cervantes'],
            ['Joseph Heller','Catch 22'],
            ['George Orwell','1984'],
            ['Khaled Hosseini','The Kite Runner']
        ]
        list_ids = range(1000,9999)
        i = 1
        while i <10:
            book_id = random.choice(list_ids)
            k = random.choice(book_options)
            book_title = k[1]
            book_author = k[0]
            book = Book(book_id, book_title, book_author)
            try:
                self.add(book)
                i+= 1
            except BadIDError:
                i-= 1
 
    def update(self, book_id, new_title, new_author):
        '''
        updates a book
        params:
            book_id - (type int)
            new_title - (type str)
            new_author - (type str)
        '''
        k = self.find(book_id)
        k.title = new_title
        k.author = new_author


class RentalsRepository(Repository):
    def __init__(self, book_repo, client_repo):
        Repository.__init__(self)
        self._books = book_repo
        self._clients = client_repo
        self.initialize_rentals()

    def initialize_rentals(self):
        for i in range(10):
            book = random.choice(self._books._repo)
            client = random.choice(self._clients._repo)
            rental = Rental(book, client)
            self.add(rental)

    def return_book(self, rent_id, date):
        k = self.find(rent_id)
        k._returned_date = date


