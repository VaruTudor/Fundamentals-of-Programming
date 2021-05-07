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
import shutil
from Repository import Repository
from domain import Book

class BookTextRepositoryLab(Repository):
    def __init__(self, file_name, file_name2):
        Repository.__init__(self)
        self._file_name = file_name
        self._file_name2 = file_name2
        self._loadFile()
        self._saveFile()


    def book_to_str(self, book):
        return str(book.id) + ',' + book.title + ',' + book.author

    def str_to_book(self, string):
        line = string.split(',') #line is a list of strs
        for c in line[2]:
            if c == "\n":
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
                self._repo.append(self.str_to_book(line))
        f.close()

    def add(self, element):
        '''
            adds an element to the repo and saves in the file
            params:
                element - will be added to self._repo (type list)
        '''
        f = open(self._file_name, 'w')
        line = self.book_to_str(element)
        f.write(line)
        f.write('\n')
        f.close()
        self._loadFile()
        self._saveFile()

    def delete(self, element_id):
        '''
            deletes an element by its id
            params:
                element_id - the id of the element (type int)     
        '''
        f = open(self._file_name, 'r')
        f2 = open(self._file_name2, 'w')
        while True:
            line = f.readline()
            if len(line) == 0:
                break
            book = self.str_to_book(line)
            if book.id == element_id:
                continue
            else:
                f2.write(line)
                # f2.write('\n')
        f.close()
        f2.close()

        # shutil.copyfile(self._file_name2, self._file_name)
        shutil.os.remove(self._file_name)

        f = open(self._file_name, 'w')
        f2 = open(self._file_name2, 'r')
        while True:
            line = f2.readline()
            print(line)
            if len(line) == 0:
                break
            f.write(line)
            f.write('\n')
        f.close()
        f2.close()

        self._loadFile()
        self._saveFile()


    def update(self, book_id, new_title, new_author):
        '''
        updates a book
        params:
            book_id - (type int)
            new_title - (type str)
            new_author - (type str)
        '''
        f = open(self._file_name, 'r')
        f2 = open(self._file_name2, 'w')
        while True:
            line = f.readline()
            if len(line) == 0:
                break
            book = self.str_to_book(line)
            if book.id == book_id:
                book.title = new_title
                book.author = new_author
                new_line = self.book_to_str(book)
                f2.write(new_line)
                f2.write('\n')
            else:
                f2.write(line)
                f2.write('\n')
        f.close()
        f2.close()

        f = open(self._file_name, 'w')
        f2 = open(self._file_name2, 'r')
        while True:
            line = f2.readline()
            if len(line) == 0:
                break
            f.write(line)
            f.write('\n')
        f.close()
        f2.close()
        self._loadFile()
        self._saveFile()


    def _saveFile(self):
        
        f = open(self._file_name, 'w')
        for book in self._repo:
            line = self.book_to_str(book)
            f.write(line)
            f.write('\n')
        f.close
