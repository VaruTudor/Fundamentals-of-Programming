from domain import Board
from errors import WrongCoordinates


class Game:
    def __init__(self, board, algorithm):
        self._board = board
        self._algorithm = algorithm

    def player_move(self, player):
        '''
        changes a square in the list with 1
        params:
            player - (list) the given coords (could be wrong)
        WrongCoordinates - players has more/less then 2 coordinates
        '''
        if len(player) != 2:
            raise WrongCoordinates
        row = player[0]
        col = player[1]
        try:
            row = int(row)
            col = int(col)
        except ValueError:
            print('you should give integers')
        self._board.move(row, col, 'b')

    def computer_move(self):
        '''will move for the computer'''
        square = self._algorithm.next_move(self._board)
        self._board.move(square[0], square[1], 'w')
        return (square[0],square[1])

    def get_board(self):
        ''' returns the board'''
        return self._board