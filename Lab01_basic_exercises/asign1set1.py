def prim(x:int):
    for d in range(2,x-1):
        if x%d==0: 
            return False
    return True
n=input('give number: ')
n=int(n)
n+=1

while(not(prim(n))):
    n+=1
print(n)
