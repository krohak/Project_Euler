# http://www.geeksforgeeks.org/prime-factorization-using-sieve-olog-n-multiple-queries/
# http://www.geeksforgeeks.org/print-all-prime-factors-of-a-given-number/
#
import numpy as np
import math
import sys

inp=sys.argv
inp=int(inp[1])

for x in range(3,int(math.sqrt(inp)),2):
    flag=0
    while inp%x==0:
        inp/=x
        if(flag==0):
            print(x)
            flag=1

if inp!=1:
    print(int(inp))
