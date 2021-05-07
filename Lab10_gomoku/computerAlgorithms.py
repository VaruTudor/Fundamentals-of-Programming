from domain import Board

class AlgorithmSimple:
    '''makes moves where it first finds an empty square'''
    def next_move(self, board):
        for row in range(15):
            for col in range(15):
                if board.get_square(row,col) == 0:
                    return (row,col)

# class 