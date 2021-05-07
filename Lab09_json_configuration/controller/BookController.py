from domain import Book
from controller.undoController import FunctionCall, Operation


class BookController:
    def __init__(self, undoController, rentalController, bookRepository):
        self._books = bookRepository
        self._rentalController = rentalController
        self._undoController = undoController

    def add_book(self, book_id, title, author):
        book = Book(book_id, title, author)
        self._books.add(book)
        
        undo = FunctionCall(self.remove_book, book_id)
        redo = FunctionCall(self.add_book, book_id, title, author)
        
        op = Operation(undo,redo)
        
        self._undoController.recordOperation(op)
        
        return book

    def remove_book(self, book_id):
        '''
            1. delete the book from the repo
        '''
        book = self._books.find(book_id)
        self._books.delete(book_id)

        undo = FunctionCall(self.add_book, book.id, book.title, book.author)
        redo = FunctionCall(self.remove_book, book_id)

        op = Operation(undo, redo)
        self._undoController.recordOperation(op)
        '''
            2. delete its rentals
        '''
        rentals = self._rentalController.filterRentals(None, book)
        for rent in rentals:
            self._rentalController.delete_rental(rent.id, True)
        return book

    def list_books(self):
        '''
        prints the list of books
        '''
        for i in self._books._repo:
            print (i)

    def update_book(self, book_id, new_title, new_author):
        self._books.update(book_id, new_title, new_author)    

    def search_book_id(self, book_id):
        for i in self._books._repo:
            if i.id == book_id:
                print (i)

    def string_matching(self, s1, s2):
        '''
        checks if s1 is a substring of s2
        params:
            s1 - (str)
            s2 - (str)
        output:
            True - s1 is a substring of s2
            False - s1 is not a substring of s2
        '''
        l1 = []
        l2 = []
        for i in s1:
            l1.append(i)
        for i in s2:
            l2.append(i)
        for i in range(len(s1)):
            if l1[i] != l2[i]:
                return False
        return True

    def search_book_title(self, title):
        for i in self._books._repo:
            if self.string_matching(title, i.title):
                print (i)

    def search_book_author(self, author):
        for i in self._books._repo:
            if self.string_matching(author, i.author):
                print (i)