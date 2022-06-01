'''
has all functionalities
'''
import random

class service:
    def digits(self,number):
        '''
        returns the digits of a number as a list
        '''
        digits = []
        i = 0
        while number !=0 :
            digits.append(number%10)
            number /= 10
            number = int(number)
            i += 1
        for i in range(0,int(len(digits)/2)):
            k = digits[len(digits)-i-1]
            digits[len(digits)-i-1] = digits[i]
            digits[i] = k
        return digits

    def cows(self, number, user_number):
        '''
        checks how many digits are correct
        params:
            number - number in the game
            user_number - number given by the user
        return:
            cows
        '''
        cows = 0
        digits_number = self.digits(number)
        digits_user_number = self.digits(user_number)
        for i in range(0,len(digits_number)):
            for j in range(0,len(digits_user_number)):
                if i != j:
                    if digits_number[i] == digits_user_number[j]: cows += 1
        return cows

    def bulls(self, number, user_number):
        '''
        checks how many digits are correct on the same position
        params:
            number - number in the game
            user_number - number given by the user
        return:
            bulls
        '''
        bulls = 0
        digits_number = self.digits(number)
        digits_user_number = self.digits(user_number)
        for i in range(0,len(digits_number)):
            for j in range(0,len(digits_user_number)):
                if i == j:
                    if digits_number[i] == digits_user_number[j]: bulls += 1
        return bulls

    def generate_number(self):
        digits = [1,2,3,4,5,6,7,8,9,0]
        number = 0
        for i in range(0,4):
            k = random.choice(digits)
            number += k
            digits.remove(k)        
            number*=10
        number /= 10
        return int(number)



        #str/ rep maybe??