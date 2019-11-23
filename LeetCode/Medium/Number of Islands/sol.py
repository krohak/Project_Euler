class Solution:

    def __init__(self):
        self.grid = []
        self.m = 0
        self.n = 0

    def numIslands(self, grid):
        self.grid = grid
        self.m = len(grid)
        if not self.m:
            return 0
        self.n = len(grid[0])
        if not self.n:
            return 0

        num_islands = 0

        explored = set()

        for i in range(self.m):
            for j in range(self.n):
                if (i,j) not in explored and grid[i][j] == "1":
                    num_islands += 1
                    self.dfs(i, j, explored)

        return num_islands

    
    def dfs(self, i, j, explored):

        explored.add((i,j))

        for (ni, nj) in self.neighbours(i,j):
            if (ni, nj) not in explored:
                self.dfs(ni, nj, explored)

    def neighbours(self, i, j):
        ngbs = []

        if i-1>=0 and self.grid[i-1][j] == "1":
            ngbs.append((i-1, j))
        if j-1>=0 and self.grid[i][j-1] == "1":
            ngbs.append((i, j-1))
        if i+1<self.m and self.grid[i+1][j] == "1":
            ngbs.append((i+1, j))
        if j+1<self.n and self.grid[i][j+1] == "1":
            ngbs.append((i, j+1))

        return ngbs