from math import sqrt

class Solution(object):
    def numSquares(self, n):
        
        L = [0 for i in range(n+1)]

        L[1] = 1

        i = 1

        while i<n+1:

            j = 1
            least_num = i

            while j <= sqrt(i):
                
                if least_num > L[(i-j**2)]:
                    least_num = L[(i-j**2)] + 1

                j+=1

            L[i] = least_num
            i+=1

        print(L)
        return L[n]



sol = Solution().numSquares(13)
print(sol)