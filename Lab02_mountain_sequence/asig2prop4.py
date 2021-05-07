def get_real_part(number):
    return number[0]
def get_complex_part(number):
    return number[1]

#1
def create_complexn(nreal,ncomp):
    return[nreal,ncomp]

def read_complexn():
    real=int(input("real:"))
    comp=int(input("complex:"))
    return create_complexn(real,comp)

def read_list():
# reads a list of coplex numbers, each given by two intigers
    n=int(input('how many complex numbers do u want:'))
    cn=[]
    for i in range(0,n):
        cn.append(read_complexn())
    return cn
#2
def display_list(NumberList):
    '''
    dispalays the list
    entrance parameters: NumberList- a list which will be displayed
    '''
    print("This are the complex numbers from the list")
    for i in range (0,len(NumberList)):
        print(NumberList[i][0],'+',NumberList[i][1],'i')

#3_prop4&11_asign2
def modulus(number):
#receives a complex number as a list and returns the square of the module
    return get_real_part(number)**2+get_complex_part(number)**2

def check_modulus(n1,n2):
#returns wether the difference of two complex number modules is positive or negative
#entrance parameters: two complex numbers given as lists
#returns true or false
    if modulus(n1)-modulus(n2)<0:
        return True
    else:
        return False


def longest_sequence(NumberList):
    '''
    checks the longest sequence of increasing modulus in a given list
    entrance parameter: NumberList-a list of complex numbers
    returns: res-the longest sequence where modulus are increasing
    '''
    count=0
    prev=0
    indexend=0
    for i in range(0,len(NumberList)-1):
        if check_modulus(NumberList[i],NumberList[i+1])==True:
            count+=1
            if count>prev:
                prev=count
                indexend=i
        if check_modulus(NumberList[i],NumberList[i+1])==False:
            count=0
    #indexend is raised by 1 bcs the comparisson is made f 2 numbers so it cunts pairs
    indexend+=1
    res=[indexend-prev,indexend+1]
    return res


def longest_mountain(NumberList):
    '''
    *mountain-first the values increase, then they decrease
    description: checks the longest sequence mountain in a given list
    entrance parameter: NumberList-a list of complex numbers
    returns: res-the longest mountain
    '''
    count=0
    ok=1 #1 if should be increasing and 0 if should be decreasing
    maximum=0
    i=0
    indexlongest=0
    while i<len(NumberList)-1:
        print (count,maximum)
        r1=get_real_part(NumberList[i])
        r2=get_real_part(NumberList[i+1])
        if ok==1:
            if r1<r2:
                count+=1
            else:
                ok=0
                i-=1
        elif ok==0:
            if r1>r2:
                count+=1
            else:
                ok=1
                if count>maximum:
                    indexlongest=i
                    maximum=count
                count=0
                i-=1
        i+=1
    return [indexlongest-maximum,indexlongest]    

def display_from(NumberList,start,end):
    for i in range (start,end):
        print(NumberList[i][0],'+',NumberList[i][1],'i')

def display_from_m(NumberList,start,end):
    for i in range (start,end+1):
        print(NumberList[i][0],'+',NumberList[i][1],'i')

#4_prop3_asign2
def check_emodulus(n1,n2):
    if modulus(n1)==modulus(n2):
        return True
    else:
        return False

def longest_esequence(NumberList):
    '''
    checks the longest sequence of equal modulus in a given list
    entrance parameter: NumberList-a list of complex numbers
    returns: res-the longest sequence where modulus are equal
    '''
    count=0
    prev=0
    indexend=0
    for i in range(0,len(NumberList)-1):
        if check_emodulus(NumberList[i],NumberList[i+1])==True:
            count+=1
            if count>prev:
                prev=count
                indexend=i
        if check_emodulus(NumberList[i],NumberList[i+1])==False:
            count=0
    #indexend is raised by 1 bcs the comparisson is made f 2 numbers so it cunts pairs
    indexend+=1
    res=[indexend-prev,indexend+1]
    return res

def StartList():
    li=[[5,5],[1,6],[2,8],[3,4],[5,3],[2,6],[1,15],[2,6],[3,4],[0,3]]
    return li

def print_menu():
    print("1. Read a list of complex numbers")
    print("2. Display the entire list of numbers")
    print("3. Display on the console the longest sequence that *observes a given property*")
    print("4. Display on the console the longest sequence where numbers having the same modulus")
    print("5. Exit the application")


def start():        
    while True:
        print_menu()
        choice=input(">")
        if(choice=='1'):
            print("for the list already available press 1 and for reading a new list press 2")
            choice2=input(">")
            if(choice2=='1'):
                k=StartList()
            if(choice2=='2'):
                k=read_list()
        if(choice=='2'):
            display_list(k)
        if(choice=='3'):
            print("choose between property 4 or 11")
            prop=input(">")
            if(prop=='4'):
                lenght=longest_sequence(k)
                display_from(k,lenght[0],lenght[1])
            if(prop=='11'):
                lenght=longest_mountain(k)
                display_from_m(k,lenght[0],lenght[1])
        if(choice=='4'):
                lenght=longest_esequence(k)
                display_from(k,lenght[0],lenght[1])
        if(choice=='5'):
            return
        else: ("wrong command")

#start()
k=[[1,0],[2,0],[3,0],[1,0],[2,0],[7,0],[12,0],[2,0],[3,0],[4,0],[5,0],[4,0],[3,0],[2,0],[1,0],[1,0],[2,0],[3,0]]
print(longest_mountain(k))
