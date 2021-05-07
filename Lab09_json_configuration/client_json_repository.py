import json
from Repository import Repository
from domain import Client

class ClientJsonRepository(Repository):
    def __init__(self, file_name):
        Repository.__init__(self)
        self._file_name = file_name
        self.load_file()
        # self.save_file()
        
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

    def update(self, client_id, new_name):
        '''
        updates a book
        params:
            book_id - (type int)
            new_title - (type str)
            new_author - (type str)
        '''
        k = self.find(client_id)
        k.name = new_name
        self.save_file()

    def save_file(self):
        books = []
        for b in self._repo:
            book = {
                "id": b.id,
                "name": b.name
            }
            books.append(book)
        with open(self._file_name, 'w') as f:
            json.dump(books, f)
        f.close()


    def load_file(self):
        f = open(self._file_name, 'r')
        data = f.read()

        # parse file
        obj = json.loads(data)
        for c in obj:
            self.add(Client(c['id'], c['name']))
        f.close()