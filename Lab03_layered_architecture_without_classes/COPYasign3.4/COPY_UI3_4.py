from COPY_nonUI3_4 import *

def print_modulo(numberList,sign,number):
    '''
    prints numbers having modulo </>/= than a number
    params:
        numberList - a list of complex numbers
        sign - '<' or '>' of '='
        number - int number
    '''
    number=float(number)
    for i in numberList:
        if sign == '<':
            if modulo(i)<number:
                print(i)
        if sign == '=':
            if modulo(i)==number:
                print(i)
        if sign == '>':
            if modulo(i)>number:
                print(i)

def print_complex(n):
    '''
    print a complex number
    params: 
        n - dictionary of 2 ints
    '''
    if n['imaginary']>=0:
        print (n['real'],'+',n['imaginary'],'i')
    else:
        print (n['real'],n['imaginary'],'i')

def list_all(numberList):
    '''
    prints a list of lists(of 2 items) as complex numbers
    params:
        numberList - the list which needs to be printed
    '''
    for i in range(0,len(numberList)):
        print_complex(numberList[i])

def list_real_from(numberList,f,t):
    '''
    prints the elements which have the real part between two given numbers
    params:
        numberList - the list of complex numbers
        f - from position
        t - to positon
    '''
    for i in range(f,t+1):
        if get_complex(numberList[i])==0:
            print(i)

def readCommand():
    '''
    Reads user s command
    output:
        tuple (command word(str),params - list of (int) values) 
    '''
    cmd = input("command: ")
    cmd = cmd.split(' ')
    command=[]
    params=[]
    for i in cmd:
        if check_word(i) or check_sign(i):
            command.append(i)
        else:
            params.append(convert_to_number(i))
    return (command,params)

def sum_from_ui(numberList,f,t):
    #prints te sum between two given positions
    k = sum_from(numberList,f,t)
    print_complex(k)

def product_from_ui(numberList,f,t):
    #prints te sum between two given positions
    k = product_from(numberList,f,t)
    print_complex(k)

def print_menu():
    print('1.Add/insert numbers to the list')
    print('2.Modify elements from the list')
    print('3.Write numbers having different properties')
    print('4.Obtain different characteristics of sub-lists (sum/product)')
    print('5.Filter the list.')
    print('6.Undo(*)')
    print('7.exit')