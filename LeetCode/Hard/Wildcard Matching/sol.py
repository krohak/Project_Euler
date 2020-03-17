class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        
        if p == s or p == '*':
            return True
        
        if p == '' or s == '':
            return False
        
        m = len(p)
        n = len(s)
        
        dp = [[ 0 for _ in range(n+1)] for _ in range(m+1)]
        
        dp[0][0] = 1
        
        for i in range(1, m+1):
            
            if p[i-1] == '*':
                j = 1
                while not dp[i-1][j-1] and j < n+1:
                    j+=1

                dp[i][j-1] = dp[i-1][j-1]
                
                while j < n+1:
                    dp[i][j] = True
                    j+=1
                
            else:
                for j in range(1, n+1):               
                    if p[i-1] == s[j-1] or  p[i-1] == '?':
                        dp[i][j] = dp[i-1][j-1]
        
        return dp[m][n]