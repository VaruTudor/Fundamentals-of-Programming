import random
from domain import*
class Service:

    def __init__(self):
        self._history=[]
        self._books=[]
        list_of_books=[['Jane Austen','Pride and Prejudice'],
                       ['William Shakespeare','Romeo & Julieta'],
                       ['William Shakespeare','Hamlet'],
                       ['William Blake','The Tiger'],
                       ['Charlotte Bronte','Jane Eyre'],
                       ['Agatha Christie','Murder on the Orient Express'],
                       ['Agatha Christe','The ABC Murders'],
                       ['Arthur Conan Doyle','The Hound of the Baskervilles'],
                       ['Arthur Conan Doyle','A Study in Scarlet'],
                       ['Charles Dickens','A Christmas Carol'],
                       ['Charles Dickens','Oliver Twist'],
                       ['Thomas Hardy','The Mayor of Casterbridge'],
                       ['J. K. Rowling','Harry Potter vol. 1'],
                       ['J. K. Rowling','Harry Potter vol. 2'],
                       ['J. K. Rowling','Harry Potter vol. 3']]
        list_of_isbns=range(1000,9999)
        for i in range(9):
            choosed_isbn=random.choice(list_of_isbns)
            choosed_book=random.choice(list_of_books)
            choosed_author=choosed_book[0]
            choosed_title=choosed_book[1]
            book=Book(choosed_isbn,choosed_author,choosed_title)
            self.add(book)
        self._history.clear()
        

    def add(self,newbook):
        for i in self._books:
            if str(i.isbn)==str(newbook.isbn):
                raise ValueError("Invalid ISBN!")
        self._history.append(self._books[:])
        self._books.append(newbook)

    def find_book_by_first_word(self,first_word):
        result=[]
        for elem in self._books:
            txt=elem.title.split(' ')
            if txt[0]==first_word:
                result.append(elem)
        return result

    def filter_books(self,first_word):
        books_to_del=self.find_book_by_first_word(first_word)
        if len(books_to_del)==0:
            raise ValueError("No match found!")
        else:
            self._history.append(self._books[:])
            for elem in books_to_del:
                self._books.remove(elem)

    def undo(self):
        if len(self._history)==0:
            raise ValueError ("No more undos!")
        self._books.clear()
        self._books.extend(self._history.pop())
