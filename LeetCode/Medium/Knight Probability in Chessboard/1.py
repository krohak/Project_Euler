class Solution:
    
    def __init__(self):
        
        self.N = 0
        self.K = 0
        self.explored = set()
        
        self.board_leaves = 0
        
    
    def knightProbability(self, N, K, r, c):
        self.N = N
        self.K = K
        
        if not K:
            return 1
        
        self.explored.add((r,c))
        
        self.dfs(r,c, 0)
        
        print(self.board_leaves, self.explored)
        return (self.board_leaves / (8**K))
    
    
    def dfs(self, r,c, depth):
        
        if 0 <= r and r < self.N and 0 <= c and c < self.N:
            if (r,c) not in self.explored:
                self.board_leaves+=1
                self.explored.add((r,c))
        else:
            return
                    
        if depth == self.K:
            return

        for (nr, nc) in self.get_neighbours(r, c):
            self.dfs(nr, nc, depth+1)
                
        
    def get_neighbours(self, r, c):
        
        ngbs = []
        
        for i in [r-2, r+2]:
            for j in [c-1, c+1]:
                ngbs.append((i,j))
                
        for i in [r-1, r+1]:
            for j in [c-2, c+2]:
                ngbs.append((i,j))
        
        return ngbs