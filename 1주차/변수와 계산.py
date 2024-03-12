import math

firstInput = int(input("첫번째 정수를 입력하시오 : "))
secondInput = int(input("두번째 정수를 입력하시오 : "))
print(firstInput,"의 ",secondInput,"승은",(firstInput**secondInput),"입니다.")

radius = float(input("반지름을 입력하시오 : "))
square = math.pi * radius ** 2
print("넓이는",square)
