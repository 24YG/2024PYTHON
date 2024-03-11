a = [1,2,3,4,5,6,7,8,9,0,["a","b","c"]]     # 리스트 생성
# a[0] a라는 리스트에서 첫번째 요소
# a[-1][0] a리스트 요소 중 마지막 요소인 리스트의 첫번째 요소
print (a[-1][0])

# 슬라이싱
print (a[0:3]) # 첫번째 요소부터 3번째 요소까지 출력
print (a[1:4]) # 두번째 요소부터 4번째 요소까지 출력

b = a[:2] # a리스트의 2번째 요소까지 b변수의 저장
print (b)

c = a[2:] # a리스트의 3번째 요소부터 끝까지 c변수에 저장
print(c)

#리스트 더하기
A = ["a","b","c"]
B = ["d","e","f"]

C = A+B # A리스트와 B리스트를 모두 더해서 변수 C에 저장
print (C)

#리스트의 길이
print(len(C)) # C리스트의 요소 개수를 출력

#리스트 값 수정

a[0] = -1 # a리스트 첫번째 요소를 -1로 수정
print(a)
