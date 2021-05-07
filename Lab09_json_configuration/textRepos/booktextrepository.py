'''
implement new kind of repo
    - program uses it in the same way as existing repository
        *has the same methods which act the same
        *program can use both type of repos
            -> repos are interchangable
    - use text-file based persitence
        *save/load cars from a text file
        *keep program status btw runs
    - 
'''
from Repository import Repository
from domain import Book

class BookTextRepository(Repository):
    def __init__(self, file_name):
        Repository.__init__(self)
        self._file_name = file_name
        self._loadFile()
        self._saveFile()

    def book_to_str(self, book):
        return str(book.id) + ',' + book.title + ',' + book.author

    def str_to_book(self, string):
        line = string.split(',') #line is a list of strs
        for c in line[2]:
            if c == "\n": ####strip
                line[2] = line[2].replace("\n", "") 
        return Book(int(line[0]), line[1], line[2])        

    def _loadFile(self):
        '''
            This function is private, so you are not allowed to call it from outside the class. Why?
                1. it does sth internal to the class, which is undocumented
                2. if it is private, it can be changed at any time
                3. if we call this directly, the memory-based repo won t work
                4. if u have an SQL repo, that also won t wok
                5. files, sql, memory are what we use to store data, services shoud not care about that
        '''
        f = open(self._file_name, 'r')
        while True:
            line = f.readline()
            if len(line) == 0:
                break
            if line != '\n':
                self.add(self.str_to_book(line))
        f.close()

    def add(self, element):
        '''
            adds an element to the repo and saves in the file
            params:
                element - will be added to self._repo (type list)
        '''
        self._repo.append(element)
        # f = open(self._file_name, 'a')
        # f.write(self.book_to_str(element))
        # f.write('\n')
        # f.close()
        self._saveFile()

    def delete(self, element_id):
        '''
            deletes an element by its id
            params:
                element_id - the id of the element (type int)     
        '''
        self._repo.remove(self.find(element_id))
        self._saveFile()

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
        self._saveFile()

    def _saveFile(self):
        
        f = open(self._file_name, 'w')
        for book in self._repo:
            line = self.book_to_str(book)
            f.write(line)
            f.write('\n')
        f.close

