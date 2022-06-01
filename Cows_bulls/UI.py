'''
here we will create a ui
'''
from service import service

class UI:
    def print_menu(self):
        #prints menu
        print('For starting a new game, press 1')
        print('For exit press 0')

    def start(self):
        s = service()
        while True:
            self.print_menu()
            command = input('>')
            if command == '1':
                print('Try to guess a number of 4 digits')
                number = s.generate_number()
                bullsN = 0
                while bullsN != 4: 
                    try:
                        number_user = int(input('enter try: '))
                        cowsN = s.cows(number,number_user)
                        bullsN = s.bulls(number,number_user)
                        print (cowsN , 'C' , bullsN , 'B')
                        if bullsN == 4: 
                            print ('YOU WON')
                    except ValueError:
                        print ('try a number')
            if command == '0':
                return