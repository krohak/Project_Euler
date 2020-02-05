class Solution:
    
    def __init__(self):
        self.m = 0
        self.n = 0
        self.board = []
        
        self.current_hor = 0
        self.current_vert = 0
        
        self.stable = True
            
    def candyCrush(self, board):
        
        self.m = len(board)
        self.n = len(board[0])
        self.board = board

        self.crush_caller()
        self.clean()
        
        while not self.stable:
            self.stable = True
            self.crush_caller()
            self.clean()
            
        return self.board
    
    def clean(self):
        
        for i in range(self.m):
            for j in range(self.n):
                if self.board[i][j] < 0:
                    self.board[i][j] = 0
                    self.gravity(i,j)
    
    def gravity(self, i, j):
        
        depth = i
        while(depth > 0):
            temp = self.board[depth-1][j]
            self.board[depth-1][j] = self.board[depth][j]
            self.board[depth][j] = temp
            depth-=1

    def crush_caller(self):
        
        for i in range(self.m):
            for j in range(self.n):
                if not self.board[i][j]==0:
                    self.crush(i,j)
                
    def crush(self, i, j):
        
        candy = self.board[i][j]

        self.crush_down(candy, i,j)
        self.crush_right(candy, i,j)
        
        self.current_vert=0
        self.current_hor=0
            

    def crush_down(self, candy, i, j):

        down = i
        while down<self.m and abs(self.board[down][j]) == abs(candy):
            self.current_vert+=1
            down+=1

        if self.current_vert >= 3:
            self.stable = False
            down = i
            while down<self.m and abs(self.board[down][j]) == abs(candy):
                self.board[down][j] = -abs(candy)
                down+=1
                        
    def crush_right(self, candy, i, j):

        right = j
        while right<self.n and abs(self.board[i][right]) == abs(candy):
            self.current_hor+=1
            right+=1
            
        if self.current_hor >= 3:
            self.stable = False
            right = j
            while right<self.n and abs(self.board[i][right]) == abs(candy):
                self.board[i][right] = -abs(candy)
                right+=1
                
board = [
    [110,5,112,113,114],
    [210,211,5,213,214],
    [310,311,3,313,314],
    [410,411,412,5,414],
    [5,1,512,3,3],
    [610,4,1,613,614],
    [710,1,2,713,714],
    [810,1,2,1,1],
    [1,1,2,2,2],
    [4,1,4,4,1014]
]

board = Solution().candyCrush(board)
print(board)