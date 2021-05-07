def perfect(x:int):
    s=0
    for d in range(1,x//2+1):
        if x%d==0:
            s+=d
    if s==x: return True
    else: return False
n=input('give number: ')
n=int(n)
n-=1
while not(perfect(n)):
    n-=1
if n!=0:
    print('primul numar perfect mai mic decat n este',n)
else: print('there is no such number')
