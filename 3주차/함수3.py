def addSub(x,y):
    return (x+y,x-y)

def myInfo() :
    name = input("이름: ")
    age = int(input("나이: ")) 
    print("이름은 %s 이고 나이는 %d 입니다"%(name,age))
    
myInfo()