class Solution:
    def minDominoRotations(self, A, B):
        
        n = len(A)
        if n<2:
            return 0
        
        top_number = A[0]
        bottom_number = B[0]

        rotations = 0
        
        for i in range(1, n):
            
            if top_number == A[i]:
                continue

            elif bottom_number == B[i]:
                continue

            if top_number == B[i]:
                rotations+=1
                A[i], B[i] = B[i], A[i]
                continue
            else:
                top_number = -1

            if bottom_number == A[i]:
                rotations+=1
                A[i], B[i] = B[i], A[i]
                continue
            else:
                bottom_number = -1

            if top_number == -1 and bottom_number == -1:
                return -1
            
        return rotations 
            
            
  