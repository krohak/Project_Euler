class Solution:

    def __init__(self):
        self.grid = []
        self.m = 0
        self.n = 0
        self.explored = set()

    def numIslands(self, grid):
        self.grid = grid
        self.m = len(grid)
        if not self.m:
            return 0
        self.n = len(grid[0])
        if not self.n:
            return 0

        islands = 0
        for i in range(self.m):
            for j in range(self.n):
                if self.grid[i][j] == "1" and (i,j) not in self.explored:
                    islands+=1
                    self.dfs(i,j)
        return islands    

    def dfs(self, i,j):
        self.explored.add((i,j))

        for (ni,nj) in self.neighbours(i,j):
            if (ni,nj) not in self.explored:
                self.dfs(ni,nj)


    def neighbours(self, i, j):
        nbs = []
        
        if i-1>=0 and self.grid[i-1][j] == "1":
            nbs.append((i-1,j))
        if i+1<self.m and self.grid[i+1][j] == "1":
            nbs.append((i+1,j))
        if j-1>=0 and self.grid[i][j-1] == "1":
            nbs.append((i,j-1))
        if j+1<self.n and self.grid[i][j+1] == "1":
            nbs.append((i,j+1))

        return nbs