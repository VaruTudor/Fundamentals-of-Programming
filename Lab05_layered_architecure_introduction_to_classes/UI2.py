from domain import Book
from service import Service

class UI2():
    def __init__(self, service):
        self._service = service

    @property
    def get_service(self):
        return self._service

    #####
    def readCommand(self):
        command = input('Give a list of commands: ')
        # commands = {'add':self.addBook,'print':self.print_list,'filter':self.filterList,'undo':self.undo}
        command = command.split(',') # commands_given will have all the list of commands
        for i in command:
            current_command = i.split(' ')
            if current_command[0] == 'add':
                self.addBook(current_command[1],current_command[2],current_command[3])
            if current_command[0] == 'print':
                self.print_list()
            if current_command[0] == 'filter':
                self.filterList(current_command[1])
            if current_command[0] == 'undo':
                self.undo()

                



    def addBook(self,isbn,author,title): # 1st functionality
        '''
        adds a book given by the user
        '''
        b = Book(isbn,author,title)
        self.get_service.addBook(b)
    
    def print_list(self): # 2nd functionality
        '''
        prints the list
        '''
        for i in self.get_service._books:
            print (i)

    def filterList(self,word): # 3rd functionality
        '''
        filters the list by deleting a book 
        '''
        self.get_service.filterList(word)

    def undo(self): # 4th functionality
        self.get_service.undo()


    def print_menu(self):
        print('1. Give commands: ')
        print('5. exit')

    def start(self):
        while True:
            self.print_menu()
            command = input('>')
            if command == '1':
                self.readCommand()
            elif command == '5':
                return
            else:
                print('Wrong command')