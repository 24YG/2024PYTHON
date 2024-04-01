def get_power(x,y):
    return x**y

def multiolicationTable(dan) :
    for i in range(1,10) :
        print("%dX%d=%d"%(dan,i,(dan*i)))
        
def factorial(x):
    fact=1
    for i in range(1,x+1):
        fact *=i
    return fact

print(factorial(10))
