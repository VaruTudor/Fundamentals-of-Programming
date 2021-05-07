class Book:
    def __init__(self, isbn, author, title):
        self._isbn=isbn
        self._author=author
        self._title=title

    @property
    def isbn(self):
        return self._isbn
    
    @property
    def author(self):
        return self._author

    @property
    def title(self):
        return self._title
    
    @isbn.setter
    def isbn(self,value):
        self._isbn=value
    
    @author.setter
    def author(self,value):
        self._author=value
    
    @title.setter
    def title(self,value):
        self._title=value

    
    def __str__(self):
        return (str(self.isbn)+"  '"+str(self.title)+"' by "+str(self.author))
    