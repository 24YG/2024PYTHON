L = int(input())
A = int(input())
B = int(input())
C = int(input())
D = int(input())

dayKorean = (A/C)
dayMath = (B/D)

if dayKorean >= dayMath :
    print(int(L-dayKorean))
else :
    print(int(L-dayMath))