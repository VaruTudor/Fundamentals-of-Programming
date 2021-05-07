import json
from Repository import Repository
from domain import Rental, Book, Client

from datetime import date

class RentalJsonRepository(Repository):
    def __init__(self, file_name, book_repo, client_repo):
        self._book_repo = book_repo
        self._client_repo = client_repo
        Repository.__init__(self)
        self._file_name = file_name
        self.load_file()
        self.save_file()
        
    def add(self, element):
        '''
            adds an element to the repo and saves in the file
            params:
                element - will be added to self._repo (type list)
        '''
        self._repo.append(element)
        self.save_file()

    def string_to_date(self, string):
        if string == '0':
            return int(string)
        else:
            string = string.split('-')
            return date(int(string[0]),int(string[1]),int(string[2]))

    def delete(self, element_id):
        '''
            deletes an element by its id
            params:
                element_id - the id of the element (type int)     
        '''
        self._repo.remove(self.find(element_id))
        self.save_file()
 
    def return_book(self, rent_id, date):
        k = self.find(rent_id)
        k._returned_date = date
        self.save_file()

    def save_file(self):
        rentals = []
        for r in self._repo:
            rental = {
                "id": r.id,
                "book id": r.book_id,
                "client id": r.client_id,
                "rented date": str(r.rented_date), 
                "returned date": str(r.returned_date)
            }
            rentals.append(rental)
        with open(self._file_name, 'w') as f:
            json.dump(rentals, f)
        f.close()


    def load_file(self):
        f = open(self._file_name, 'r')
        data = f.read()

        # parse file
        obj = json.loads(data)
        for r in obj:
            book = self._book_repo.find(r['book id'])
            client = self._client_repo.find(r['client id'])
            rental = Rental(book, client)
            rental._rental_id = r['id']
            rental._rented_date = self.string_to_date(r['rented date'])
            rental._returned_date = self.string_to_date(r['returned date'])
            self.add(rental)
        f.close()

