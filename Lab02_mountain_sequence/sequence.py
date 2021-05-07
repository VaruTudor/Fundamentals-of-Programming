li=[1,2,3,5,2,3,0,5,6]
def rule(n1,n2):
    if n1<n2:
        return True
    else:
        return False

def sequence(k):
    count=0
    prev=0
    indexend=0
    for i in range(0,len(k)-1):
        if rule(k[i],k[i+1]):
            count+=1
        else: 
            if count>prev:
                prev=count
                indexend=i
            count=0
    res=[indexend-prev,indexend]
    return res
def start():
    li=[1,2,3,5,2,3,0,5,6]
    print(sequence(li))
start()
