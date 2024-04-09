# Prog: sortInt.py
def sort (x,y,z) :
    A=[x,y,z]
    A.sort()
    return (A[0],A[1],A[2])
def main () :
    x = int (input () )
    y = int (input () )
    z = int (input () )
    p,q,r = sort (x,y,z)
    print ('sorted as : %d, %d, %d\n'%(p,q,r))
main ()