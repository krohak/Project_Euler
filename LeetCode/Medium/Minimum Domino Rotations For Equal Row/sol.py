class Solution:
    def minDominoRotations(self, A, B):
        
        n = len(A)
        if n<2:
            return 0
        
        top_number = A[0]
        bottom_number = B[0]
        
        
        c1 = self.takePath(n, top_number, A, B)
        c2 = self.takePath(n, bottom_number, A, B)
        
            
        if c1 == float('inf') and c2== float('inf'):
            return -1
        
        return min(c1, c2)
            
            
    
    def takePath(self, n, number, A, B):
        
        c1 = 0
        top_cost = 0
        bottom_cost = 0
        
        for i in range(n):

            if not A[i] == number and not B[i] == number:
                c1 = float('inf')
                break

            elif A[i] == number and not B[i] == number:
                bottom_cost +=1

            elif not A[i] == number and B[i] == number:
                top_cost +=1

        return c1 if c1==float('inf') else min(bottom_cost, top_cost)