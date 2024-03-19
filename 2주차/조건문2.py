price = int(input("정가를 입력하시오: "))
if price >= 100 :
    dis_rate = 0.85
    print("10층에서 사은품을 받아가세요.")
else :
    dis_rate = 0.90
    dis_price = dis_rate * price
    dif = int(100-price)
    print("현재 구입액은 %d만원 이고 %.2f 만큼 더 구입하면 사은품을 받을수있습니다."%(price,dif))
print("할인된 상품의 가격=", dis_price)

