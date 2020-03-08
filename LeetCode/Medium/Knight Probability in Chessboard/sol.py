class Solution:
    
        
    def knightProbability(self, N, K, r, c):
        
        dp = [ [ 0 for _ in range(N) ] for _ in range(N)]
        
        dp[r][c] = 1
        
        for _ in range(K):
            dp_next = [ [ 0 for _ in range(N) ] for _ in range(N)]
            
            for i, row in enumerate(dp):
                for j, cell in enumerate(row):
                    for ni, nj in self.get_neighbours(i, j):
                        if 0 <= ni and ni < N and 0<= nj and nj < N:
                            dp_next[ni][nj] += cell/8
            
            dp = dp_next
        
        return sum([sum(row) for row in dp ])
        
    
    
    def get_neighbours(self, i, j):
        
        for x in [i-2, i+2]:
            for y in [j-1, j+1]:
                yield((x,y))         
        
        for x in [i-1, i+1]:
            for y in [j-2, j+2]:
                yield((x,y))
        