N=int(input())
A=list(map(int,input().split()))
v=int(input())
Nv=0

for i in A :
    if v == i :
        Nv +=1
print(Nv)

