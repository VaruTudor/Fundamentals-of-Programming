'''
    - will contain the main classes
'''
#############3 clear the code pls!
class Point:
    '''
    every point is a line from the game on papper
    '''
    def __init__(self, x, y):
        if (type(x) != int or type(y) != int):
            raise Exception('must be an integer')
        else:
            self._x = x
            self._y = y
            # self._content = 0
            
    @property
    def x(self):
        return self._x
    @property
    def y(self):
        return self._y
    
    @x.setter
    def x(self, x):
        self._x = x
    @y.setter
    def y(self, y):
        self._y = y
    
    def __repr__(self):
        return (str(self.x) + ',' + str(self.y))

    def __str__(self):
        return (str(self.x) + ',' + str(self.y)) + '  '
        

class Game_point(Point):
    
    def __init__(self, x, y):
        Point.__init__(self, x, y)
        self.content = 0


class Line:

    def __init__(self, index, lenght):
        if type(lenght) != int or type(index) != int:
            raise Exception('must be an integer')
        else:
            self._line = []
            self._index = index
            self._lenght = lenght
            self.initialize_line(self._index, self._lenght)
    
    def initialize_line(self, index, lenght):
        for p in range(lenght):
            self._line.append(Point(index,p))

    def __str__(self):
        s = ''
        for p in self._line:
            s += str(p)
            print(type(p), ',', p)
        return s

    def __repr__(self):
        s = ''
        for p in self._line:
            s += str(p)
        return s

    def get_line(self):
        return self._line




class Game_line(Line):
    def __init__(self, index, lenght):
        Line.__init__(self, index, lenght)

    def initialize_line(self, index, lenght):
        if index % 2 == 0:
            for p in range(lenght):
                if p % 2 == 0:
                    self._line.append(Point(index,p))
                else:
                    self._line.append(Game_point(index,p))
        else:
            for p in range(lenght):
                if p % 2 == 0:
                    self._line.append(Game_point(index,p))
                else:
                    self._line.append(Point(index,p))

# l = Game_line(3, 3)
# print(l)
# print(l._index)
# # print (type(l) == Game_line)
# print(l.get_line())

class Sqare:
    
    def __init__(self, size):
        if type(size) != int:
            raise Exception('must be an integer')
        elif size > 15:
            raise Exception('you would get bored')
        else:
            self._square = []
            self.initialize_square(size)

    def initialize_square(self, size):
        for l in range(size):
            self._square.append(Line(l,size))

    def __str__(self):
        s = ''
        for l in self._square:
            s += str(l) + '\n'
        s = s[:-1]
        return s

    def __repr__(self):
        s = ''
        for l in self._square:
            s += str(l) + '\n'
        s = s[:-1]
        return s

    def find_point(self, x, y):
        try:
            return self._square[x]._line[y]
        except IndexError:
            print ('the square is a bit smaller')

    def get_line(self, number):
        for l in self._square:
            if l._index == number:
                return l

    def get_square(self):
        return self._square

class Game_square(Sqare):

    def __init__(self, size):
        size = 2*size+1
        Sqare.__init__(self, size)

    def initialize_square(self, size):
        for l in range(size):
            line = Game_line(l,size)
            if line._index == 0 or line._index == 2*size:
                for p in line.get_line():
                    if (type(p) == Game_point):
                        p._content = 1
            elif line._index % 2 == 1:
                line.get_line()[0]._content = 1
                line.get_line()[size-1]._content = 1
            self._square.append(line)



k = [1,2]
print(k[0])
p = Game_square(2)
print (p)

# class move:
    
#     def __init__(self, square, x, y, direction):
#         self._square = square
#         self._x = x
#         self._y = y
#         if direction not in ('up','down','left','right'):
#             raise Exception('what direction is that?????')
#         self._direction = direction
#         self.make_move()

#     def make_move(self):
#         p = self._square.find_point(self._x, self._y)
#         id self._direction == 'up':
#             p.[self._direction] = 1

