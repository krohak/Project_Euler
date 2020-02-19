class Solution:
    
    
    def __init__(self):
        self.m = 0 # no of rows
        self.n = 0 # no of columns 
        self.board = []
        self.negative_candies = True
    
    def candyCrush(self, board):
        """
        :type board: List[List[int]]
        :rtype: List[List[int]]
        """
        self.m = len(board)
        if not self.m:
            return board
        
        self.n = len(board[0])
        if not self.n:
            return board
        
        self.board = board
        
        while self.negative_candies:
            self.crush_candies()    
        return self.board
    
    
    def crush_candies(self):
        for x in range(self.m):
            for y in range(self.n):
                if not self.board[x][y] == 0:
                    self.check_consecutive(x, y)
        
        self.negative_candies = False
        for x in range(self.m):
            for y in range(self.n):
                if self.board[x][y] < 0:
                    self.negative_candies = True
                    self.board[x][y] = 0
                    self.gravity(x,y)        
    
    def gravity(self, x, y):
        for i in range(x, 0, -1):
            self.board[i][y], self.board[i-1][y] = self.board[i-1][y], self.board[i][y]
        
    
    def check_consecutive(self, x, y):
        
        candy = self.board[x][y]
        counter = 1
        
        # go downwards
        for i in range(x+1, self.m):
            if abs(self.board[i][y]) == abs(candy):
                counter +=1
            else:
                break
        
        # mark to crush 
        if counter >= 3:
            for i in range(x, x+counter):
                self.board[i][y] = -abs(candy)
        
        counter = 1
        
        # go right
        for j in range(y+1, self.n):
            if abs(self.board[x][j]) == abs(candy):
                counter +=1
            else:
                break
        
        if counter >= 3:
            for j in range(y, y+counter):
                self.board[x][j] = -abs(candy)
        
        