from texttable import Texttable
from errors import OutsideBoard, Overwrite

class Board:
    def __init__(self):
        # the board is 15 by 15 with 0 on every position
        self._moves = 0
        self._board = [[0 for _ in range (15)]for _ in range(15)]

    #board status
    def win(self):
        '''
        we check if there are 5 non 0 squares in a line
        '''
        counter_1 = 0
        counter_2 = 0
        # rows 
        for r in self._board:
            for pos in r:
                if pos == 1:
                    counter_1 += pos
                    counter_2 = 0
                elif pos == -1:
                    counter_2 += pos
                    counter_1 = 0
                else:
                    counter_1 = 0 
                    counter_2 = 0

                if counter_1 == 5:
                    return counter_1
                elif counter_2 == -5:
                    return counter_2  

        board = self._board
        # columns
        for c in range(15):
            for r in range(15):
                pos = board[r][c]
                if pos == 1:
                    counter_1 += pos
                    counter_2 = 0
                elif pos == -1:
                    counter_2 += pos
                    counter_1 = 0
                else:
                    counter_1 = 0 
                    counter_2 = 0
                if counter_1 == 5:
                    return counter_1
                if counter_2 == -5:
                    return counter_2  

        # main diagonal
        for i in range(15):
            for d in range(14-i,15): 
                pos = board[d-(14-i)][d]
                if pos == 1:
                    counter_1 += pos
                    counter_2 = 0
                elif pos == -1:
                    counter_2 += pos
                    counter_1 = 0
                else:
                    counter_1 = 0 
                    counter_2 = 0
                if counter_1 == 5:
                    return counter_1
                if counter_2 == -5:
                    return counter_2
        for i in range(13,-1,-1):
            for d in range(14-i,15):
                pos = board[d][d-(14-i)]
                if pos == 1:
                    counter_1 += pos
                    counter_2 = 0
                elif pos == -1:
                    counter_2 += pos
                    counter_1 = 0
                else:
                    counter_1 = 0 
                    counter_2 = 0
                if counter_1 == 5:
                    return counter_1
                if counter_2 == -5:
                    return counter_2  
        
        # secondary diagonal
        for i in range(31):
            if i < 15:
                for d in range(i+1):
                    pos = board[d][i-d]
                    if pos == 1:
                        counter_1 += pos
                        counter_2 = 0
                    elif pos == -1:
                        counter_2 += pos
                        counter_1 = 0
                    else:
                        counter_1 = 0 
                        counter_2 = 0
                    if counter_1 == 5:
                        return counter_1
                    if counter_2 == -5:
                        return counter_2 
                else:
                    for d in range (i-14,15):
                        pos = board[d][i-d]
                        if pos == 1:
                            counter_1 += pos
                            counter_2 = 0
                        elif pos == -1:
                            counter_2 += pos
                            counter_1 = 0
                        else:
                            counter_1 = 0 
                            counter_2 = 0
                        if counter_1 == 5:
                            return counter_1
                        if counter_2 == -5:
                            return counter_2 

    def tie(self):
        '''
        we check if the game is not won, but also there is no 0 square
        '''
        if self.win() == False and self._moves == 15*15:
            return True
        else:
            return False

    def move(self, row, col, symbol):
        '''
        adds a symbol to one of the squares
        params:
            row - (int)
            col - (int)
            symbol - ('b' or 'w')
        '''
        # ensure row, col are in board
        if row < 0 or row >= 15 or col < 0 or col >= 15:
            raise OutsideBoard

        # check not to overwrite
        if self._board[row][col] != 0:
            print (self._board[row][col])
            raise Overwrite

        d = {'b':1, 'w':-1}
        self._board[row][col] = d[symbol]
        self._moves += 1

    def reset(self):
        """Clear the board (set all position to 0)."""
        self._board = [[0 for _ in range(15)] for _ in range(15)]

    def get_square(self, row, col):
        """
        Get the value at a coord.
        params:
            row - (int) (must be in range(0,15))
            col - (int) (must be in range(0,15))
        """
        
        if row < 0 or row >= 15 or col < 0 or col >= 15:
            return 0 # raise error later
        return self._board[row][col]

    def get_board(self):
        return self._board

    def __str__(self):
        '''we create a textable where every square will be a square in the representation'''
        t = Texttable()
        d = {0:' ',1:'b', -1:'w'}
        for row in self._board:
            row_copy = row[:]
            for j in range(15):
                row_copy[j] = d[row[j]]
            t.add_row(row_copy)
            
        return t.draw()