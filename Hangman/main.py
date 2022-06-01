from repo import Repository
from initialState import Board
from controller import Controller
from ui import UI

repo = Repository('sentences.txt')
board = Board(repo)
cont = Controller(board)
ui = UI(cont)

ui.start()