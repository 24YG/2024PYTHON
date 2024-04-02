N = int(input())
B=[350.34,230.90,190.55,125.30,180.90]

for i in range(N):
    A= list(map(int,input().split()))
    sum=0
    for i in range(5) :
        sum += A[i]*B[i]
    print("$%.2f"%(sum))