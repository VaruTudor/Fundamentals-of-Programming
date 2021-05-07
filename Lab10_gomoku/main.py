from computerAlgorithms import *
from domain import Board
from ui import UI
from controller import Game
from gui import GUI

print('1.UI')
print('2.GUI')
command = input('>')


alg = AlgorithmSimple()
board = Board()

game = Game(board, alg)

if command == '1':
    ui = UI(game)
    ui.start()
elif command == '2':
    ui = GUI(game)
    ui.start()
else:
    print('wrong command')