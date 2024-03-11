print("hello world" * 10) # hello world 10번 반복 

a = "tukorea"
print(a[:3])

print("hello \nworld")

print('%d / %d = %.2f ' % (200,100,2.0)) # %n.mf()에서 n은 n만큼의 자릿수 확보 / m은 소수점 m번째 자리까지 출력
print("{0:d} {1:d} {2:d}".format(100,200,300)) 

print("뉴\n라인")
print("tab\t키")
print("백스페 \b이스")
print("문자열\"따옴표\"출력")

print('강아지 이름')
for name in("멍멍이","푸근이","햅삐") :
    print(name,end=",")
    
print("\n%.2f * %.2f = %.2f" %(3.0,3.0,9.0))

print("파이썬에 온건 환영합니다.\n파이썬은 쉽습니다\n파이썬으로 빅데이터,인공지능 어쩌구")

print(2+3)
print(2-3)
print(2*3)
print(2/3)

print("%s \n%s \n%s"%("\"한국공학대학교\"","\"컴퓨터 공학부\"","\"조영광\""))
print("{0:s} \n{1:s} \n{2:s}".format("\"한국공학대학교\"","\"컴퓨터 공학부\"","\"조영광\""))
