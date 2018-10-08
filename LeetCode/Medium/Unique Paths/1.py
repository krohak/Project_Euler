class Solution(object):
    def uniquePaths(self, m, n):

        if m==0 or n==0:
            return 0

        L = {}

        i = 0
        while i<m:
            j = 0
            while j<n:
                L[(i,j)] = 0
                j+=1
            i+=1

        L[0,0] = 1

        i = 0
        while i<m:
            j = 0
            while j<n:
                
                if i-1>=0:
                    L[(i,j)]+=L[(i-1,j)]

                if j-1>=0:
                    L[(i,j)]+=L[(i,j-1)]

                j+=1
            i+=1
        
        # print(L)
        return L[(m-1,n-1)]


sol = Solution().uniquePaths(3,2)

sol = Solution().uniquePaths(7,3)

# sol = Solution().uniquePaths(1,1)

print(sol)