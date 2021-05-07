'''
    CLIENT TEXT REPOSITORY
'''

from Repository import Repository
from domain import Rental

class RentalTextRepository(Repository):
    def __init__(self, file_name, book_repo, client_repo):
        self._book_repo = book_repo
        self._client_repo = client_repo
        Repository.__init__(self)
        self._file_name = file_name
        self._load_file()
        self._save_file()


    def str_to_rental(self, string):
        '''
        transforms a string into an object of type Rental
        params:
            string - (type string) a line in the file
        '''
        string = string.split(',')
        string[4] = string[4].replace('\n','')
        book = self._book_repo.find(int(string[1]))
        client = self._client_repo.find(int(string[2]))
        rental = Rental(book,client)
        rental._rental_id = int(string[0])
        rental._rented_date = string[3]
        rental._returned_date = string[4]
        return rental

    def rental_to_str(self, rental):
        return str(rental.id) + ',' + str(rental.book_id) + ',' + str(rental.client_id) + ',' + str(rental.rented_date) + ',' + str(rental.returned_date)

    def add(self, element):
        '''
            adds an element to the repo and saves in the file
            params:
                element - will be added to self._repo (type list)
        '''
        self._repo.append(element)
        self._save_file()

    def delete(self, element_id):
        '''
            deletes an element from the repo and saves the file
            params:
                element_id - the id of the element (type int) 
        '''
        self._repo.remove(self.find(element_id))
        self._save_file()

    def return_book(self, rent_id, date):
        k = self.find(rent_id)
        k._returned_date = date
        self._save_file()
        

    def _load_file(self):
        '''
            adds to the repository every client present in file
        '''
        f = open(self._file_name, 'r')
        while True:
            line = f.readline()
            if len(line) == 0:
                break
            rental = self.str_to_rental(line)
            self._repo.append(rental)
        f.close()

    def _save_file(self):
        '''
            adds from repository to the file
        '''
        f = open(self._file_name, 'w')
        for rental in self._repo:
            f.write(self.rental_to_str(rental))
            f.write('\n')
        f.close()