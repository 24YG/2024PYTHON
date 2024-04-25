def numOf6():
    numbers=[i for i in range(100) if i%2==0 and i%3 == 0]
    return numbers

def 홀짝():
    numbers=["짝수" if i%2==0 else "홀수" for i in range(10)]
    return numbers

def sumTarget():
    basic=[10, 20, 30, 40, 50]
    numbers=[sum(basic[:i+1]) for i in range(len(basic))]
    return numbers

