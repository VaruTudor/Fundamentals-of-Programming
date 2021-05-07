'''
here it will be written the book class
'''

class Book():
    def __init__(self,isbn,author,title):
        '''
        initializes a book
        params:
            isbn - unique string
            author - string
            title - string
        '''
        self._isbn = isbn
        self._author = author
        self._title = title

    @property
    def Isbn(self):
        # gets the isbn
        return self._isbn

    @Isbn.setter
    def Isbn(self, u_code):
        # sets a new isbn with u_code
        # u_code (string) is the only param
        self._isnb = u_code

    @property
    def Author(self):
        # gets the author
        return self._author

    @Author.setter
    def Author(self, author_name):
        # sets a new author with author_name
        # author_name (string) is the only param
        self._author = author_name

    @property
    def Title(self):
        #gets the author
        return self._title

    @Title.setter
    def Title(self, title_name):
        #sets a new title with title_name
        #title_name (string) is only param
        self._title = title_name

    def __str__(self):
        return str(self.Isbn) + ' ' + str(self.Author) + ', ' + str(self.Title)

def test_book():
    book1 = Book('1' , 'Ion Creanga' , 'Amintiri din copilarie')
    assert book1.Isbn == '1' and book1.Author == 'Ion Creanga' and book1.Title == 'Amintiri din copilarie'
    book1.Author = 'Mihai Eminescu'
    assert book1.Author == 'Mihai Eminescu'
    book1.Title = '132'
    assert book1.Title == '132'

test_book()