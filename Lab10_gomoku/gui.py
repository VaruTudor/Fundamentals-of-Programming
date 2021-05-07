from controller import Game
from domain import Board
from computerAlgorithms import AlgorithmSimple
from errors import WrongCoordinates, OutsideBoard, Overwrite
import tkinter 

class GUI:
    def __init__(self, game):
        self.window = tkinter.Tk()
        self.window.geometry('510x600')
        self.window.title(' G O M O K U ')
        self._game = game
        label = tkinter.Label(self.window, text="", font=("Arial Bold", 14), width=42, height=7, bg='#ff7817', fg="#ff4d21")
        label.place(x=0, y=420)
        btn = tkinter.Button(self.window, text="restart",font=("Arial Bold", 10), width=63, height=1, bg='#b3b3b3', fg="#ff7817", command=self.start)
        btn.place(x=0, y=572)

    def clicked(self, row, col):
        '''
        returns the coords where the player move should be made and changes the button
        '''
        if self.win_status() not in (-5,5) and self.tie_status() == False:
            label = tkinter.Label(self.window, text=chr(9679), font=("Arial Bold", 10), width = "3", bg='#b3b3b3', fg="#000000")
            label.grid(column=col, row=row)   
            self._game.player_move([row,col])
            if self.win_status() == 5:
                label = tkinter.Label(self.window, text="You master this game, go play solitaire now",
                font=("Arial Bold", 14), width=42, height=6, bg='#ff7817', fg="#703f16")
                label.place(x=0, y=420)
                return
            computer_moves = self._game.computer_move()
            label = tkinter.Label(self.window, text=chr(9679), font=("Arial Bold", 10), width = "3", bg='#b3b3b3', fg="#ffffff")
            label.grid(column=computer_moves[1], row=computer_moves[0])
            if self.win_status() == -5:
                label = tkinter.Label(self.window, text="Computer won, you should train more", 
                font=("Arial Bold", 14), width=42, height=6, bg='#ff7817', fg="#703f16")
                label.place(x=0, y=420)
                return
            if self.tie_status() == True:
                label = tkinter.Label(self.window, text="You are at least as smart as my algorithm. Congrats ... i guess",
                font=("Arial Bold", 14), width=42, height=6, bg='#ff7817', fg="#703f16")
                label.place(x=0, y=420)
                return

    def win_status(self):
        return self._game.get_board().win()

    def tie_status(self):
        return self._game.get_board().tie()

    def start(self):
        self._game.get_board().reset()
        for row in range (15):
            for col in range(15):
                btn = tkinter.Button(self.window, text=" ", font=("Arial Bold", 10), width = "3", bg='#b3b3b3', fg="#ff4d21", command = lambda row=row, col=col :self.clicked(row,col))
                btn.grid(column=col, row=row)
        label = tkinter.Label(self.window, text="", font=("Arial Bold", 14), width=42, height=7, bg='#ff7817', fg="#ff4d21")
        label.place(x=0, y=420)
        self.window.mainloop()