def fibonacci(x):
    if x<0:
        print('it s not a fibonacci number')
    elif x==0:
        return 1
    elif x==1:
        return 2
    else:
        return fibonacci(x-1)+fibonacci(x-2)
n=int(input('give a number:'))
c=1
while(fibonacci(c)<n):
    c+=1
print(fibonacci(c))
