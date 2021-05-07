import random
from domain import Book
'''
This module has the fuctionalities of the program
1.Add a new book to the list.
'''

class Service:
    def __init__(self):
        # initialises a list of books
        self._history = []
        self._books = []
        book_options = [
            ['André Brink','A Dry White Season'],
            ['Nikos Kazantzakis','Zorba the Greek'],
            ['Kathleen Winter','Annabele'],
            ['Malinda Lo','Ash'],
        ]
        list_isbns = range(100,999)
        for i in range(10):
            r_isbn = random.choice(list_isbns)
            k = random.choice(book_options)
            r_title = k[0]
            r_author = k[1]
            book = Book(r_isbn,r_title,r_author)
            try:
                self.addBook(book)
            except ValueError:
                continue
        self._history.clear()

    def addBook(self, book):
        '''
        adds a book to the list of books
        params:
            book - (type Book) a book which will be added to the list
        raise ValueError if there is another book with the same isbn
        '''
        for i in self.get_books:
            if int(i.Isbn) == int(book.Isbn):
                raise ValueError ("There is another book with the same isnb")
        self.get_history.append(self.get_books[:])
        self.get_books.append(book)

    @property
    def get_books(self):
        return self._books
    
    @property
    def get_history(self):
        return self._history

    def filterList(self, word):
        '''
        Book objects where title starts with (word) are deleted from the list.
        params:
            word - str
        '''
        self.get_history.append(self.get_books[:])
        i = 0
        while i< len(self.get_books):
            l = self.get_books[i]
            k = l.Title
            k = k.split(' ')
            if k[0] == word:
                self.get_books.pop(i)
                i-=1
            i+=1

    def undo(self):
        '''
        undoes the last operation
        '''
        if len(self.get_history) == 0:
            raise ValueError ('no more undos')
        self.get_books.clear()
        self.get_books.extend(self.get_history.pop())

    def clear(self):
        self.get_books.clear()

def test_addBook():
    l = Service()  
    l.clear()
    book_1 = Book('11','ME','Poezii')
    l.addBook(book_1)
    # print (l.get_books)
    assert l.get_books == [book_1] 
    book_2 = Book('1','2','3')
    l.addBook(book_2)
    assert l.get_books == [book_1,book_2]
    # print(l.get_books)

def test_filterList():
    l = Service()  
    l.clear()
    book_1 = Book('11','ME','Poezii de')
    book_2 = Book('1','2','3')
    l.addBook(book_1)
    l.addBook(book_2)
    l.filterList('3')
    # print (l.get_books)
    assert l.get_books == [book_1]


def tests():
    test_addBook()
    test_filterList()

tests()