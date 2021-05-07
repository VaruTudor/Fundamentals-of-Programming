
class Controller:
    def __init__(self, board):
        self.board = board
        self.sentence = self.board.choose_sentence()
        self.sentence = self.sentence.replace('\n','')
        self.transformed_sentence = self.board.sentence_to_hangman(self.sentence)
        self.computer = ''
        self.hangman = 0

    def end_game(self):
        if self.sentence == self.transformed_sentence or self.hangman == 7:
            return False
        return True

    def initialize_game(self):
        self.sentence = self.board.choose_sentence()
        self.sentence = self.sentence.replace('\n','')
        self.transformed_sentence = self.board.sentence_to_hangman(self.sentence)
        self.computer = ''
        self.hangman = 0

    def player_move(self, letter):
        change = 0
        for i in range (0,len(self.sentence)-1):
            if self.sentence[i] == letter:
                change = 1
                self.transformed_sentence = self.board.change_letter(self.sentence,self.transformed_sentence,letter)
        if change == 0:
            self.hangman += 1
        