def print_baggage_items (*arg1,**arg2) :
    A=(arg1)
    B=(arg2)
    A=list(A)
    print("#단일품목\n %s\n%s\n%s"%(A[0],A[1],A[2]))
    for i in arg2 :
        pass
    
print_baggage_items('laptop', 'camera', 'charger', socks=8, pants=2, shirts=4)
