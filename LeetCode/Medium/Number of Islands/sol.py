class Solution:
    
    def numIslands(self, grid):
        
        m = len(grid)
        if not m: return 0
        
        n = len(grid[0])
        if not n: return 0
        
        connectedComponents = 0
        self.visited = set()
        self.grid = grid
        
        for i in range(m):
            for j in range(n):
                if self.grid[i][j]=="1" and (i,j) not in self.visited:
                    connectedComponents+=1
                    self.dfs(i, j)
        return connectedComponents
    
    def dfs(self, i, j):
        self.visited.add((i, j))
        for (ni, nj) in self.getNeighbors(i,j):
            if (ni,nj) not in self.visited:
                self.dfs(ni, nj)
    
    def getNeighbors(self, i, j):
        checkGrid = lambda x,y: 0<=x and x<len(self.grid) and 0<=y and y<len(self.grid[0]) and self.grid[x][y]=="1"
        return [ ( i+x, j+y) for x, y in [[0, +1], [0, -1], [-1, 0], [+1, 0]] if checkGrid(i+x,j+y)  ]
        