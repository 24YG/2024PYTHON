def average_list (li):
    return sum(li)/len(li)  

def main():
    List = list(map(int,input("평균을 구할 정수들을 띄어쓰기로 구분해 입력하시오 : ").split()))
    print("%.2f"%(average_list(List)))
    
main()

