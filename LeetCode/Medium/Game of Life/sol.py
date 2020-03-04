TO_DIE = '1'
TO_LIVE = '0'

class Solution:
    
    def __init__(self):
        self.board = []
        self.m = 0
        self.n = 0
    
    def gameOfLife(self, board):
        """
        Do not return anything, modify board in-place instead.
        """
        
        self.m = len(board)
        self.n = len(board[0])
        if not self.m*self.n:
            return board
        
        self.board = board
        
        for i in range(self.m):
            for j in range(self.n):
                self.check_neighbours(i,j)
        
        for i in range(self.m):
            for j in range(self.n):
                if self.board[i][j] == TO_DIE:
                    self.board[i][j] = 0
                elif self.board[i][j] == TO_LIVE:
                    self.board[i][j] = 1
                
    
    def check_neighbours(self, i, j):
        
        live_count = 0
        for x in range(i-1, i+2):
            for y in range(j-1, j+2):
                if x>= 0 and x<self.m and y>=0 and y<self.n and not (x==i and y==j):
                    if self.board[x][y] == 1 or self.board[x][y] == TO_DIE:
                        live_count+=1
                        
        if self.board[i][j] and (live_count < 2 or live_count > 3):
            self.board[i][j] = TO_DIE

        elif not self.board[i][j] and live_count == 3:
            self.board[i][j] = TO_LIVE
                
                
        
        