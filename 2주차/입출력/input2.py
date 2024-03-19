import math

rad = float(input("구의 반지름을 입력하시오(cm): "))
print("구의 면적은 %.8f 입니다"%(rad**3 * 3/4 * math.pi))