class Solution:
    def spiralOrder(self, matrix):
        m = len(matrix)
        if not m: return []
        
        n = len(matrix[0])
        if not n: return []
        
        self.matrix = matrix        
        up, down, left, right = 0, m-1, 0, n-1
        self.i, self.j = 0, 0
        
        answer = []
        while not (left > right or up > down):
            l2r = self.leftToRight(left, right)
            answer.extend(l2r)
            up+=1
            u2d = self.upToDown(up, down)
            answer.extend(u2d)
            right-=1
            
            if not (left > right or up > down):
                r2l = self.rightToLeft(left, right)
                answer.extend(r2l)
                down-=1
                d2u = self.downToUp(up, down)
                answer.extend(d2u)
                left+=1
            
        return answer
    
    
    def leftToRight(self, left, right):
        self.j = right
        return [ self.matrix[self.i][j] for j in range(left, right+1) ] 
    
    def upToDown(self, up, down):
        self.i = down
        return [ self.matrix[i][self.j] for i in range(up, down+1) ]
    
    def rightToLeft(self, left, right):
        self.j = left
        return [ self.matrix[self.i][j] for j in range(right, left-1, -1) ]        
    
    def downToUp(self, up, down):
        self.i = up
        return [ self.matrix[i][self.j] for i in range(down, up-1, -1) ]