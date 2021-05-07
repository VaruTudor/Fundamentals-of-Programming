import random
from datetime import date

class Client:
    def __init__(self, client_id, client_name):
        self._id = client_id
        self._name = client_name

    @property
    def id(self):
        return self._id
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, set_name):
        self._name = set_name

    def __str__(self):
        return 'id ' + str(self.id) + ' : ' + self.name
    
    def __repr__(self):
        return 'id ' + str(self.id) + ' : ' + self.name


class Book:
    def __init__(self, book_id, book_title, book_author):
        self._id = book_id
        self._title = book_title
        self._author = book_author
    
    @property
    def id(self):
        return self._id
    @property
    def title(self):
        return self._title
    @property
    def author(self):
        return self._author

    @title.setter
    def title(self, set_title):
        self._title = set_title

    @author.setter
    def author(self, set_author):
        self._author = set_author

    def __repr__(self):
        return "Book({},'{}','{}')".format(self.id, self.title, self.author)

    def __str__(self):
        return 'id: '+ str(self.id) + ' ' + self.title + ' by ' + self.author


class Rental:
    def __init__(self, book, client, returned_date = 0):
        list_rental_ids = range(1000,9999)
        self._rental_id = random.choice(list_rental_ids)
        self._book_id = book.id
        self._client_id = client.id
        self._rented_date = date.today()
        self._returned_date = returned_date

    @property
    def id(self):
        return self._rental_id 
    @property
    def book_id(self):
        return self._book_id
    @property
    def client_id(self):
        return self._client_id
    @property
    def rented_date(self):
        return self._rented_date
    @property
    def returned_date(self):
        return self._returned_date 

    # @returned_date.setter
    # def returned_date(self, set_date):
    #     self.returned_date = set_date
    
    def __str__(self):
        return 'id: '+ str(self.id) + ', book id:' + str(self.book_id) + ', client id: ' + str(self.client_id) + ' rented at ' + str(self.rented_date) + ' returned at ' + str(self.returned_date)