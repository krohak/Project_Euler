# 3
'''
Mathematical Solution
Suppose base is the good base we need to finally ask, k is the number of 1 after the hexadecimal conversion, 
then we can get the following equation: 

base^(k-1) + base^(k-2) + ... + base^1 + base^0 = N ... [1] 
base^k + base^(k-1) + ... + base^2 + base^1 = N * base 

Therefore, we can get: 
base ^k - base^0 = (base - 1) * N
N = (base^k - 1) / (base - 1) .... [2] 

From [1], you can get: 

base ^ (k-1) < N < (base+1) ^ (k-1) ... 
Polynomial expansion can prove the inequality base on the right 

base < (k-1)-th root of N < base + 1 ... [3] 

according to [2] And [3], we can get the final answer by traversing the number of bits
'''
import math

class Solution3(object):
    def smallestGoodBase(self, n):
        """
        :type n: str
        :rtype: str
        """        
        num = int(n)
        thisLen = int(math.log(num,2)) + 1
        while thisLen > 2:
            # from equation [3], we have
            thisBase = int(num ** (1.0/(thisLen - 1)))
            # from equation [2], we have
            if num * (thisBase - 1) == (thisBase ** thisLen) - 1:
                return str(thisBase)
            thisLen -= 1
        return str(num - 1)