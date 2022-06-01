'''
    functionality
'''
from domain import Sqare, Game_square

class Game:

    def __init__(self, size, player1, player2):
        # game_square must be an object of type Game_square
        self._game_square = Game_square(size)

    def move(self, point, name):
        '''
            should change the _content of the game point with the name of the player
            params:
                point - (type Game_point)
                name - (type str)
            also: change only if the previous content is 0
        '''
        pass

    # think about getters and setters - finding a point in game square

    
