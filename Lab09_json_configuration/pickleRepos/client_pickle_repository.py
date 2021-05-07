import pickle
from Repository import Repository
from domain import Client

class ClinetPikleRepository(Repository):
    def __init__(self, file_name):
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

    def delete(self, element_id):
        '''
            deletes an element by its id
            params:
                element_id - the id of the element (type int)     
        '''
        self._repo.remove(self.find(element_id))
        self.save_file()

    def update(self, book_id, new_name):
        '''
        updates a book
        params:
            book_id - (type int)
            new_title - (type str)
            new_author - (type str)
        '''
        k = self.find(book_id)
        k.name = new_name
        self.save_file()

    def save_file(self):
        f = open(self._file_name, 'wb')
        pickle.dump(self._repo, f)
        f.close()

    def load_file(self):
        f = open(self._file_name, 'rb')
        try:
            self._repo = pickle.load(f)
        except EOFError:
            f.close()
        f.close()