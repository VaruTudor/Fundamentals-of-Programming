def prim(x:int):
    for d in range(2,x//2):
        if x%d==0: 
            return False
    return True
n=input('give number: ')
n=int(n)
n+=1
while (not(prim(n))) or (not(prim(n+2))):
    n+=1
p1,p2=n,n+2
print(str(p1)+" "+str(p2))
