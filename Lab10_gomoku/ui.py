from controller import Game
from domain import Board
from computerAlgorithms import AlgorithmSimple
from errors import WrongCoordinates, OutsideBoard, Overwrite

class UI:
    def __init__(self, game):
        self._game = game

    def menu(self):
        print(' G O M O K U ')
        print('let your brain storm')
        print('1. start game')
        print('2. exit')

    def win_status(self):
        return self._game.get_board().win()

    def tie_status(self):
        return self._game.get_board().tie()

    def print_board(self):
        print (self._game.get_board())

    def start(self):
        while True:
            self.menu()
            command = input('choose: ')
            if command == '1':
                self._game.get_board().reset()
                while self.win_status() not in (-5,5) and self.tie_status() == False:   
                    #checks whether the game ends by win or tie
                    self.print_board()
                    player = input('your move ').split(' ')
                    if player[0] == 'exit' and player[1] == 'game':
                        break
                    try:
                        self._game.player_move(player)
                    except WrongCoordinates:
                        print ('you inserted more/less coords')
                        continue
                    except OutsideBoard:
                        print ('your move is outside the board, learn to count before playing GOMOKU')
                        continue
                    except Overwrite:
                        print ('there was already something there, try another move')
                        continue
                    except Exception:
                        continue
                    if self.win_status() == 5:
                        self.print_board()
                        print ('You master this game, go play solitaire now')
                        break
                    self._game.computer_move()
                    if self.win_status() == -5:
                        self.print_board()
                        print ('Computer won, you should train more')
                        break  
                if self.tie_status() == True:
                    self.print_board()
                    print ('You are at least as smart as my algorithm. Congrats ... i guess')
            elif command == '2':
                return
            else:
                print('wrong command')

