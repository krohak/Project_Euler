class Solution:
    def maximalSquare(self, matrix: list) -> int:
        m = len(matrix)
        n = len(matrix[0])
        
        dp = [ [0]*n for _ in range(m) ]
        maxSide = 0
        
        for i in range(m):
            dp[i][0] = int(matrix[i][0])
            maxSide = max(dp[i][0], maxSide)
        
        for j in range(n):
            dp[0][j] = int(matrix[0][j])
            maxSide = max(dp[0][j], maxSide)
                
        for i in range(1, m):
            for j in range(1, n):
                if int(matrix[i][j]):
                    dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1
                    maxSide = max(dp[i][j], maxSide)
        
        return maxSide**2
        