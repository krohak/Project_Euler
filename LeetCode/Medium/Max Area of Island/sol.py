class Solution:
    
    def __init__(self):
        
        self.grid = []
        
        self.explored = set()
        self.connected_components = {} #key:0, val:size
        self.component = 0
        self.component_size = 0
        
        self.m = 0
        self.n = 0
    
    
    def maxAreaOfIsland(self, grid: [[int]]) -> int:
        
        self.m = len(grid)
        if not self.m:
            return 0
        
        self.n = len(grid[0])
        if not self.n:
            return 0
        
        self.grid = grid
        
        for i in range(self.m):
            for j in range(self.n):
                if not (i,j) in self.explored and grid[i][j] == 1:
                    self.component_size = 0
                    self.component+=1

                    self.dfs(i,j)
                    
                    self.connected_components[self.component] = self.component_size
        
        return max(self.connected_components.values()) if self.connected_components.values() else 0
            
    def dfs(self, i, j):
        
        self.component_size += 1
        self.explored.add((i,j))
        
        for ni, nj in self.neighbours(i,j):
            if self.grid[ni][nj] == 1 and not (ni,nj) in self.explored:
                self.dfs(ni, nj)
            
    
    def neighbours(self, i, j):
        
        ngbs = []
        
        if i > 0:
            ngbs.append((i-1, j))
        if j > 0:
            ngbs.append((i, j-1))
            
        if i < self.m-1:
            ngbs.append((i+1,j))
        
        if j < self.n-1:
            ngbs.append((i, j+1))
        
        return ngbs