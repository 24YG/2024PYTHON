items={"비누":[3,2],"칫솔":[5,4],"샴푸":[2,1],"치약":[4,4],"로션":[5,3]}

niceItems=[]
noItems=[]
for i,j in items.items():
    if j[0]>=4 and j[1]>=4 :
        niceItems.append(i)
    else:
        noItems.append(i)
        
print("판매가능 상품은 : ",end="")
for i in niceItems:
    print("%s"%(i),end=" ")

