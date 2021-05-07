import math
from nonUI3_4 import *
from UI3_4 import *

def start():
    NumberList=[[5,3],[3,4],[2,0],[3,4],[5,0],[2,6],[1,15],[2,6],[3,4],[0,3]]
    undoList=[]
    print('if u want to start a new list press 2')
    print('if u want to keep the list which is already in the program press any button different than 2')
    if input('>') =='2':
        NumberList.clear() 
    while True:
        print_menu()
        choice=input('>')
        if choice=='1':
            cmd=readCommand()
            command=cmd[0] # has the command as a string
            params=cmd[1] # has a list of 3 el., the first two are the complex number and the last is position where to insert
            if command[0]=='add':
                if isinstance(params[0],int):
                    k=params[0]
                    params[0]=[k,0] 
                try:
                    add_number(NumberList,params[0],undoList)
                except IndexError:
                    print ('The second parameter is not a complex number. Try again.')
            elif(command[0]=='insert'):
                try:
                    insert_number(NumberList,params[0],params[1],undoList)
                except IndexError:
                    print ('The second parameter is not a complex number. Try again.')
            else:
                print("wrong command")
        if choice=='2':
            cmd2=readCommand()
            command=cmd2[0] # has the command as a string
            params=cmd2[1] # has a list of el.
            if(command[0]=='remove' and len(command)==1):
                try:
                    remove(NumberList,params[0],undoList)
                except TypeError:
                    print ('The number u gave is not in the list')
            elif(command[0]=='remove' and len(command)==2):
                try:
                    remove_from(NumberList,params[0],params[1],undoList)
                except IndexError:
                    print ('The command must respect the syntax: remove <start position> to <end position>')
                except TypeError:
                    print ('At least one number does not represent a position in the list. Try another one.')
            elif(command[0]=='replace'):
                try:
                    isinstance(params[0],list) and isinstance(params[1],list) and len(params[0])==2 and len(params[1])==2
                    if isinstance(params[0],list) and isinstance(params[1],list) and len(params[0])==2 and len(params[1])==2:
                        replace(NumberList,params[0],params[1],undoList)
                    else:
                        print('the complex numbers do not respect the syntax: <number> +/- <number> i')
                except IndexError:
                    print ('The command must respect the syntax: replace <old number> with <new number>') 
            else:           
                print("wrong command")
        if choice=='3':
            cmd3=readCommand()
            command=cmd3[0] # has the command as a string
            params=cmd3[1] # has a list of el.
            if command[0]=='list' and len(command)==1 and len(params) == 0:
                list_all(NumberList)
            elif command[0]=='list' and command[1]=='real':
                try:
                    list_real_from(NumberList,params[0],params[1])
                except IndexError:
                    print ('The syntax must be: list real <start position> to <end position> where both numbers given must be within the length of the list')
                except TypeError:
                    print ('At least one of the given numbers was not integer')
            elif command[0]=='list' and command[1]=='modulo':
                try:
                    print_modulo(NumberList,command[2],params[0])
                except IndexError:
                    print ('The syntax must be: list modulo [ < | = | > ] <number>')
                except TypeError:
                    print ('The given number was not integer')
            else:
                print("wrong command")
        if choice=='4':
            cmd4=readCommand()
            command=cmd4[0]
            params=cmd4[1]
            if command[0] == 'sum':
                try:
                    sum_from_ui(NumberList,params[0],params[1])
                except IndexError:
                    print ('the syntax must be: sum <start position> to <end position> where both numbers given must be within the length of the list')
                except TypeError:
                    print ('at least one of the given numbers is not an integer')
            elif command[0] == 'product':
                try:
                    product_from_ui(NumberList,params[0],params[1])
                except IndexError:
                    print ('the syntax must be: product <start position> to <end position> where both numbers given must be within the length of the list')
                except TypeError:
                    print ('at least one of the given numbers is not an integer')
            else:
                print("wrong command")
        if choice=='5':
            cmd5=readCommand()
            command=cmd5[0]
            params=cmd5[1]
            if command[0]=='filter' and command[1]=='real' and len(params) == 0:
                filter_real(NumberList,undoList)
            elif command[0]=='filter' and command[1]=='modulo' and (command[2] == '>' or command[2] == '<' or command[2] == '=') and len(params) == 1:
                try:
                    filter_modulo(NumberList,params[0],command[2],undoList)
                except TypeError:
                    print('the number must be an integer')
            else:
                print("wrong command")
        if choice=='6':
            try:
                undo_list(NumberList,undoList)
            except ValueError:
                print ("no more undos")
        if choice=='7':
            return

start()