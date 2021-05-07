from controller import Game
from domain import Board
from computerAlgorithms import AlgorithmSimple
from errors import WrongCoordinates, OutsideBoard, Overwrite
import pygame


class Button():
    def __init__(self, color, x, y, width, height, text=''):
        self.color = color
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = text

    def draw(self, win):
        #Call this method to draw the button on the screen
        pygame.draw.rect(win, self.color, (self.x,self.y,self.width,self.height),0)
        
        if self.text != '':
            font = pygame.font.SysFont('comicsans', 60)
            text = font.render(self.text, 1, (0,0,0))
            win.blit(text, (self.x + (self.width/2 - text.get_width()/2), self.y + (self.height/2 - text.get_height()/2)))

    def isOver(self, pos):
        #Pos is the mouse position or a tuple of (x,y) coordinates
        if pos[0] > self.x and pos[0] < self.x + self.width:
            if pos[1] > self.y and pos[1] < self.y + self.height:
                return True
            
        return False

class GUI:
    def __init__(self, game):
        pygame.init()
        self.window = pygame.display.set_mode((500,500), pygame.FULLSCREEN)
        self._game = game
        for row in range (15):
            for col in range(15):
                None
                # btn = Button(self.window, text=" ", font=("Arial Bold", 10), width = "3", bg='#a8ffad', fg="#ff4d21")
                # btn.grid(column=col, row=row)

    def win_status(self):
        return self._game.get_board().win()

    def tie_status(self):
        return self._game.get_board().tie()