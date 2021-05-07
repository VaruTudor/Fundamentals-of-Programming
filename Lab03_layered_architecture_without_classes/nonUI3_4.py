import math
### all non-UI functions
def create_Cnumber(r,c):
    '''
    creates a complex number
    output:
        a list where the first elem is the real part and the second the complex one
    '''
    return [int(r),int(c)]

def get_real(n):
    '''
    returns the real part of a complex number given
    '''
    return n[0]

def get_complex(n):
    '''
    returns the real part of a complex number given
    '''
    return n[1]

def add_number(NumberList,number,undoList): 
    '''
    description: adds a number to the list
    params:
        NumberList- the list of numbers
        number- a list of two integers (representing the parts of a complex number)
    output:
        The updated list, The undo list
    '''  
    undoList.append(NumberList[:])
    NumberList.append(number)
    return (NumberList,undoList)

def insert_number(NumberList,number,position,undoList): 
    '''
    description: inserts a number to the list at a given position
    params:
        NumberList - the list of numbers
        number - a list of two integers (representing the parts of a complex number)
        positon - an integer which tells where in the list should insert
    output:
        The updated list
    '''
    undoList.append(NumberList[:])
    NumberList.insert(position,number)
    return (NumberList,undoList)

def remove(NumberList,pos,undoList):
    '''
    description: removes a number from the list at a given position
    params:
        NumberList - the list of numbers
        pos - an integer which tells whih position to be removed
    output:
        The updated list
    '''
    undoList.append(NumberList[:])
    del NumberList[pos]
    return (NumberList,undoList)

def list_to_int(n):
    if len(n)==1:
        return n[0]

def remove_from(NumberList,f,t,undoList):
    '''
    description: removes numbers from a list
    params:
        NumberList - the list of numbers
        f - from where to remove(integer)
        t - until where to remove(integer)
    output:
        The updated list
    '''
    undoList.append(NumberList[:])
    i=f
    k=t-f+1 # counts the amount of steps
    for j in range(0,k):
        del NumberList[i]
    return (NumberList,undoList)

def find(NumberList,number):
    '''
    finds the positions of a complex number in a list
    output:
        pos - list of positions
    '''
    pos=[]
    for i in range(0,len(NumberList)):
        if NumberList[i]==number:
            pos.append(i)
    return pos

def check_word(w):

    '''
    checks if a string is a word
    output:
        True - string is a word
        False - string is not a word
    '''
    for i in w:
        if i.isalpha()==False:
            return False
    return True

def check_sign(w):

    '''
    checks if a string is a sign
    output:
        True - string is a sign
        False - string is not a sign
    '''
    sign=['<','>','=']
    for i in range(0, len(sign)):
        if w==sign[i]:
            return True    
    return False

def convert_to_number(s):
    '''
    returns all numbers in a string
    params:
        s - word as a string
    output:
        numbers - a list of all the numbers in s (or just one number(int) if s is contains just one number)
    '''
    num='1234567890'
    numbers=[] 
    k = 0 #checks for "-"
    ok = 1
    number = 0
    for i in s:
        if num.find(i)<0:
            ok = 0
            break
    if ok == 0:
        for i in s:
            if i == '0' and number == 0:
                numbers.append(int('0'))
            elif num.find(i) >= 0:
                number = number + int(i)
                number*=10
            else:   
                if number!=0:
                    number /= 10
                    number = int(number)
                    if k == 1:
                        numbers.append(-number)
                        k = 0
                    else:
                        numbers.append(number)
                number=0
            if i == '-':
                k=1
        if number!=0:
            number /= 10
            number = int(number)
            if k == 1:
                numbers.append(-number)
            else:
                numbers.append(number)
    else:
        return int(s)
    return numbers

def replace(NumberList,n1,n2,undoList):

    '''
    description: replaces items with other items(given) in a list
    params:
        NumberList - the list of numbers
        n1 - a list/ an integer which must be replaced
        n2 - a list/ an integer which will replace
    output:
        The updated list
    '''
    undoList.append(NumberList[:])
    pos=find(NumberList,n1)
    for i in range (0,len(pos)):
        remove(NumberList,pos[i],[])
        insert_number(NumberList, n2, pos[i],[])
    return (NumberList,undoList)

def modulo(n):
    '''
    calculates the modulo of a complex number
    params:
        n - the complex number(list of 2 el)
    output:
        the modulo(float)
    '''
    return math.sqrt(get_real(n)**2+get_complex(n)**2)

def filter_real(numberList,undoList):
    '''
    removes non-real elements
    params:
        numberList - a list of complex number represented as lists
    output:
        the updated list
    '''
    undoList.append(numberList[:])
    i=0
    while i<len(numberList):
        if get_complex(numberList[i])!=0:
            remove(numberList,i,[])
        else:
            i+=1
    return (numberList,undoList)

def filter_modulo(numberList,modulus,sign,undoList):
    '''
    removes numbers with modulo <,> then
    params:
        numberList - a list of complex number represented as lists
        modulus - the number to be compared with
        sign - < or > or = (as a string)
    output:
        the updated list
    '''
    undoList.append(numberList[:])
    i=0
    while i<len(numberList):
        if sign == '>' and modulo(numberList[i])<=modulus:
            remove(numberList,i,[])
        elif sign == '<' and modulo(numberList[i])>=modulus:
            remove(numberList,i,[])
        elif sign == '=' and modulo(numberList[i])!=modulus:
            remove(numberList,i,[])
        else:
            i+=1
    return (numberList,undoList)    

def sum_from(numberList,f,t):
    '''
    writes the sum between two given positions
    params:
        numberList - a list of complex number represented as lists
        f - from where
        t - to where
    output:
        the sum as a tuple
    '''
    s_real=0
    s_complex=0
    for i in range(f,t+1):
        s_real+=get_real(numberList[i])
        s_complex+=get_complex(numberList[i])
    return (s_real,s_complex)
    
def product_from(numberList,f,t):

    '''
    writes the product between two given positions
    params:
        numberList - a list of complex number represented as lists
        f - from where
        t - to where
    output:
        the product as a tuple
    '''
    x=get_real(numberList[f])
    y=get_complex(numberList[f])
    u=get_real(numberList[f+1])
    v=get_complex(numberList[f+1])
    p_real = x*u - y*v
    p_complex = x*v + y*u
    for i in range(f+2,t+1):
        u = get_real(numberList[i])
        v = get_complex(numberList[i])
        p_real = p_real*u - p_complex*v
        p_complex = p_real*v + p_complex*u
    return (p_real,p_complex)

def undo_list(numberList,undoList):
    '''
    undo the last operation
    params:
        numberList(list) - a list of numbers
        undoList(list) - a list of lists
    output:

    '''
    if len(undoList) == 0:
       raise ValueError
    numberList.clear()
    numberList.extend(undoList.pop())
    return (numberList,undoList)
