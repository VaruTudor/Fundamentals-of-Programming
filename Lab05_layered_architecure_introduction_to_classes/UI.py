from domain import Book
from service import Service

class UI:
    def __init__(self, service):
        self._service = service

    @property
    def get_service(self):
        return self._service

    def addBook(self): # 1st functionality
        '''
        adds a book given by the user
        '''
        isbn = input('isnb: ')
        author = input('author: ')
        title = input('title: ')
        b = Book(isbn,author,title)
        self.get_service.addBook(b)
    
    def print_list(self): # 2nd functionality
        '''
        prints the list
        '''
        for i in self.get_service._books:
            print (i)

    def filterList(self): # 3rd functionality
        '''
        filters the list by deleting a book 
        '''
        word = input('the word for filtering: ')
        self.get_service.filterList(word)

    def undo(self): # 4th functionality
        self.get_service.undo()

    def print_menu(self):
        print('1. Add a new book to the list.')
        print('2. Show the list of books on the console.')
        print('3. Filter the list.')
        print('4. Undo the last operation that modified program data.')
        print('5. exit')
        

    def start(self):
        while True:
            self.print_menu()
            command = input('>')
            if command == '1':
                try:
                    self.addBook()
                except ValueError as e:
                    print(e)
            elif command == '2':
                self.print_list()
            elif command == '3':
                self.filterList()
            elif command == '4':
                try:
                    self.undo()
                except ValueError as e:
                    print(e)
            elif command == '5':
                return
            else:
                print('Wrong command')