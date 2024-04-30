contact={}
def addContact() :
    name = input("이름을 입력하시오 : ")
    if name in contact :
        print("이미 %s의 전화번호가 저장되어 있습니다."%(name))
    else :
        phNumber = input("전화번호를 입력하시오 : ")
        contact[name]=phNumber
    
def delContact() :
    name = input("삭제할 이름을 입력하시오.")
    del contact[name]
    print("%s의 연락처를 삭제 하였습니다."%(name))
    
def findContact() :
    name = input("연락처를 찾을 이름을 입력하시오. : ")
    if name in contact :
        print(contact[name])
    else :
        print("%s 의 연락처는 존재하지 않습니다.")
        
def printContact() : 
    name = input("출력할 이름을 입력하시오 : ")
    if name in contact :
        print("%s의 전화번호:%s"%(name,contact[name]))
    else :
        print("%s의 전화번호가 존재하지 않습니다.")
def menu() :
    print(" 1. 연락처 추가 \n"
          "2. 연락처 삭제 \n",
          "3. 연락처 찾기 \n",
          "4. 연락처 출력 \n",
          "5. 종료",
          )
    
def main():
    while True :
        menu()
        user = int(input("메뉴 항목을 선택하시오. : "))
        if user == 1:
            addContact()
        elif user == 2:
            delContact()
        elif user == 3:
            findContact()
        elif user == 4:
            printContact()
        else :
            break
        
if __name__ == "__main__" :
    main()