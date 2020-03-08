class Solution:
    def climbStairs(self, n: int) -> int:
        
        minus_one = 2
        minus_two = 1
        
        if n==1:
            return 1
        
        elif n==2:
            return 2
        
        for _ in range(3, n+1):
            steps = minus_one + minus_two
            minus_two = minus_one
            minus_one = steps
        
        return steps
            
        