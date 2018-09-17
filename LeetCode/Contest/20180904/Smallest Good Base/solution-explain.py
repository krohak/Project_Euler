# 1
'''
Naive Solution 
According to the meaning of the topic, it is easy to write the checkBase(base,n) function. For a given base, determine whether the base is a good base of a given number n, and the time complexity of this judgment function is O(log N).

The search space is naturally 0 to n - 1. 

Then, we can write an algorithm with a time complexity of O(N log N).
'''

class Solution(object):
    def smallestGoodBase(self, n):
        """
        :type n: str
        :rtype: str
        """
        def checkBase(base, n):
            """
            Given a base, check whether it is a good base.
            Time complexity is O(log N)
            """
            current = 1
            while current < n:
                current = current * base + 1
            return current == n
        thisNum = int(n)
        for i in range(2, thisNum):
            if checkBase(i, thisNum):
                return str(i)
        return str(thisNum - 1)


'''
However, the range given by n is [3, 10^18], and even the method of O(N log N) is unacceptable.
'''

# 2 (not working!!!!!!!!!!! probably wrong)
'''
Better Solution
Naive Solution searches the entire solution space by traversing the base. In addition, we can traverse the entire solution space by traversing the number of bits after the conversion, so that the search scope is much smaller. 

We assume that in goodbase, the final number is 11...1, where there are k 1. Then the range of k is [2, log(n, 2)]. Then we use the binary search To determine whether there is such an integer base, so that n is converted to a number consisting of k 1s. 

The time complexity of the algorithm is O(logN * logN)
'''

import math
class Solution2(object):
    def smallestGoodBase(self, n):
        """
        :type n: str
        :rtype: str
        """
        def getAnsofBase(length, base):
            """
            Convert 11...11 (base `base`) to base 10
            """
            ans = 1
            for i in range(length-1):
                ans = ans * base + 1
            return ans

        def findLengthBase(length, n):
            """
            Check whether there exist a base such that
            n in base `base` == 111...111 (length's 1s)
            """
            start, end = 0, n/2
            while start <= end:
                mid = (start + end) / 2
                target = getAnsofBase(length, mid)
                if target == n:
                    return mid
                elif target < n:
                    start = mid + 1
                else:
                    end = mid - 1
            return -1

        num = int(n)
        thisLen = int(math.log(num,2)) + 1
        while thisLen > 2:
            retVal = findLengthBase(thisLen, num)
            if retVal != -1:
                return str(retVal)
            thisLen -= 1
        return str(num - 1)


# 3
'''
Mathmatical Solution
Suppose base is the good base we need to finally ask, k is the number of 1 after the hexadecimal conversion, then we can get the following equation: 

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

class Solution3(object):
    def smallestGoodBase(self, n):
        """
        :type n: str
        :rtype: str
        """        
        num = int(n)
        thisLen = int(math.log(num,2)) + 1
        while thisLen > 2:
            # from equation [3], we havve
            thisBase = int(num ** (1.0/(thisLen - 1)))
            # from equation [2], we have
            if num * (thisBase - 1) == thisBase ** thisLen - 1:
                return str(thisBase)
            thisLen -= 1
        return str(num - 1)