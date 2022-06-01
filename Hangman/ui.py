from controller import Controller
from errors import NoWords,SmallWord,Duplicate

class UI:
    def __init__(self, cont):
        self.cont = cont

    def print(self):
        print('1. add sentence')
        print('2. play game')
        print('3. exit game')

    def start(self):
        while True:
            self.print()
            command = input('>')
            if command == '2':
                self.cont.initialize_game()
                while self.cont.end_game():
                    print(self.cont.transformed_sentence)
                    give_letter = input ('give letter: ')
                    self.cont.player_move(give_letter)
                    if self.cont.hangman == 0: print('hangman status: ')
                    elif self.cont.hangman == 1: print('hangman status: h')
                    elif self.cont.hangman == 2: print('hangman status: ha')
                    elif self.cont.hangman == 3: print('hangman status: han')
                    elif self.cont.hangman == 4: print('hangman status: hang')
                    elif self.cont.hangman == 5: print('hangman status: hangm')
                    elif self.cont.hangman == 6: print('hangman status: hangma')
                    print('\n')
                if self.cont.hangman == 7:
                    print('hangman status: hangman')
                    print('you lost')
                else:
                    print('you won')                    
            elif command == '1':
                sentence = input('give ur sentence: ')
                try:
                    self.cont.board.repo.write_sentence(sentence)
                except NoWords:
                    print('there must be at least 2 words')
                except SmallWord:
                    print ('words minumum lenght is 3')
                except Duplicate:
                    print ('Dupicate sentence')
            elif command == '3':
                return
            else:
                print('wrong command')
            