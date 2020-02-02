class Solution:

    def __init__(self):
        self.regions = 0
        self.connected_components = {}
        self.explored = set()
        self.board = []
        self.m = 0
        self.n = 0

    # def solve(self, board: List[List[str]]) -> None:
    def solve(self, board):
        """
        Do not return anything, modify board in-place instead.
        """
        
        self.board = board

        self.m = len(board)
        if not self.m:
            return
        self.n = len(board[0])
        if not self.n:
            return

        for i in range(self.m):
            for j in range(self.n):
                if board[i][j] == "O" and (i,j) not in self.explored:
                    self.regions+=1
                    self.connected_components[self.regions] = []
                    self.dfs(i,j)

        for _, nodes in self.connected_components.items():
            if nodes:
                self.flip_o_region(nodes)
    

    def dfs(self,i,j):

        safe = self.check_safety(i,j)
        if not safe and self.connected_components[self.regions]!=None:
            self.connected_components[self.regions] = self.connected_components.get(self.regions,[]) + [(i,j)]
        else:
            self.connected_components[self.regions] = None
        self.explored.add((i,j))

        for ni, nj in self.neighbours(i,j):
            if self.board[ni][nj] == "O" and (ni,nj) not in self.explored:
                self.dfs(ni,nj)
    
    def neighbours(self, i, j):
        ngbs = []

        if i-1>=0 and self.board[i-1][j] == "O":
            ngbs.append((i-1, j))
        if j-1>=0 and self.board[i][j-1] == "O":
            ngbs.append((i, j-1))
        if i+1<self.m and self.board[i+1][j] == "O":
            ngbs.append((i+1, j))
        if j+1<self.n and self.board[i][j+1] == "O":
            ngbs.append((i, j+1))

        return ngbs

    def check_safety(self, i, j):
        if i==0 or j==0 or i==self.m-1 or j==self.n-1:
            return True
        return False


    def flip_o_region(self, nodes):
        for (i,j) in nodes:
            self.board[i][j] = "X"



# connected_components = {
#     1:[(3,2),(1,2)],
#     2:None
# }
# board = [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]
# board = [["O","O","O"],["O","O","O"],["O","O","O"]]
# Solution().solve(board)
# print(board)