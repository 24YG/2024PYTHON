def readList():
    nlist = []
    flag = True
    while flag :
        number = int(input("숫자를 입력하시오: "))
        if number < 0:
            flag = False
        else :
            nlist.append(number)
        return nlist
if __name__ == "__main__":
    print (readList())