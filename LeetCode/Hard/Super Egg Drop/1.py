import math
class Solution:
    def superEggDrop(self, K: int, N: int) -> int:
        
        if K==1:
            return N
        
        if K > math.floor(math.log(N,2)):
            return math.floor(math.log(N,2))+1
        
        else:

            first_moves = math.floor(math.log(N,2))
            first_part = 2**first_moves
            
            second_part = N+1-first_part
            
            second_moves = math.floor(math.log(second_part,2))
            
            return first_moves+second_moves