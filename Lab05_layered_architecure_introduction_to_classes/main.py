from UI import UI
from UI2 import UI2
from service import Service

def main():
    choice = input ('choose between the representations 1 or 2:  ')
    s = Service()
    if choice == '1':
        ui = UI(s)
        ui.start()
    elif choice == '2':
        ui = UI2(s)
        ui.start()
    else:
        print ('You must choose btw 1 or 2')
    



main()