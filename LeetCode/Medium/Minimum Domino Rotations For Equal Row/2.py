class Solution:
    def minDominoRotations(self, A, B):
        
        n = len(A)
        if n<2:
            return 0
        
        top_number = A[0]
        bottom_number = B[0]
        
        rotations = 0
        
        for i in range(1, n):
            
            top_bool = bottom_bool = True
            if top_number == A[i]:
                pass
            elif top_number == B[i]:
                rotations+=1
            else:
                top_bool = False
            
            if bottom_number == B[i]:
                pass
            elif bottom_number == A[i]:
                rotations+=1
            else:
                bottom_bool = False
            
            if not top_bool and not bottom_bool:
                return -1
            
        return rotations 
            
            
        