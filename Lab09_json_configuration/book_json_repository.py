import json
from Repository import Repository
from domain import Book

class BookJsonRepository(Repository):
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
        self.save_file()

    def save_file(self):
        books = []
        for b in self._repo:
            book = {
                "id": b.id,
                "title": b.title,
                "author": b.author
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
        for b in obj:
            self.add(Book(b['id'], b['title'], b['author']))
        f.close()
