def sequence(k):
    count=0
    ok=1 #1 if should be increasing and 0 if should be decreasing
    maximum=0
    i=0
    while i<len(k)-1:
        r1=k[i]
        r2=k[i+1]
        print(r1,'-',r2,' i=',i,' count=',count, 'ok=',ok)
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
        print(r1,'-',r2,' i=',i,' count=',count, 'ok=',ok)
        i+=1
    rang=[indexlongest-maximum,indexlongest]
    return rang
def start():
    li=[5,1,2,3,5,2,1,0,3,0,5,6]
    print(sequence(li))
start()
