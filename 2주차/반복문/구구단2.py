n=2

while n<=5 :
    d=1
    while d<=9 :
        print("%d*%d=%d"%(n,d,n*d))
        d+=1
    n+=1

while n<=5 :
    for i in range(1,10) :
        print("%d*%d=%d"%(n,i,n*i))
    n+=1