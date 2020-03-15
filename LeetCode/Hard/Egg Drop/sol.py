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
            min_moves_floor = 1
            for n in range(2, N+1):
                
                while min_moves_floor < n+1 and dp[k-1][min_moves_floor-1] < dp[k][n-min_moves_floor]:
                    min_moves_floor+=1

                dp[k][n] = 1+ dp[k-1][min_moves_floor-1]
                        
        return dp[K][N]