from math import sqrt

class Solution(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """

        L = [0 for ns in range(n+1)]

        L[1] = 1

        for i in range(1,n+1):

            # min accross reverse dag
            min_terms_add = n
            for j in range(1,int(sqrt(i))+1):
                
                prev_node = i - (j**2)

                terms_add = L[prev_node]

                # print(i, j ,prev_node, terms_add)

                if  terms_add < min_terms_add:
                    min_terms_add = terms_add

            L[i] = min_terms_add+1

        # print(L)
        return L[n]


sol = Solution().numSquares(12)
print(sol)