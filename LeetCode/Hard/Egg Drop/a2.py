class Solution:
    def superEggDrop(self, K: int, N: int) -> int:
        
        dp = [ [ float('inf') for n in range(N+1) ] for k in range(K+1)]
        
        for n in range(N+1):
            dp[0][n] = 0
            dp[1][n] = n
        
        for k in range(K+1):
            dp[k][0] = 0
            dp[k][1] = 1
        
        
        for k in range(2, K+1):
            for n in range(2, N+1):
                
                bottom_floor = 0
                top_floor = n
                
                while(bottom_floor < top_floor):
                    
                    mid =  (bottom_floor+top_floor)//2
                    
                    bottom_moves = dp[k-1][mid-1]
                    top_moves = dp[k][top_floor-mid]
                    
                    if top_moves > bottom_moves:
                        bottom_floor = mid+1
                        
                    else:
                        top_floor = mid
                        
                
                dp[k][n] = 1 + max(dp[k-1][bottom_floor-1], dp[k][n-bottom_floor])
                        
        return dp[K][N]