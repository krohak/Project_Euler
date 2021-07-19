class Solution:
    def spiralOrder(self, matrix):
        
        #m rows, n cols
        m = len(matrix)
        if not m: return []
        n = len(matrix[0])
        if not n: return []
        self.matrix = matrix
        
        top, bottom = 0, m-1
        left, right = 0, n-1
        
        self.i, self.j = 0, 0
        
        spiral = []
        while top <= bottom and left <= right:
            spiral.extend([ n for n in self.printRight(left, right) ])
            top+=1
            spiral.extend([ n for n in self.printDown(top, bottom) ])
            right-=1
            
            if top <= bottom and left <= right:
                spiral.extend([ n for n in self.printLeft(left, right) ])
                bottom-=1
                spiral.extend([n for n in self.printUp(top, bottom) ])
                left+=1
            
        return spiral
    
    def printRight(self, left, right):
        for y in range(left, right+1):
            self.j = y
            yield self.matrix[self.i][y]
            
    def printLeft(self, left, right):
        for y in range(right, left-1, -1):
            self.j = y
            yield self.matrix[self.i][y]
            
    def printDown(self, top, bottom):
        for x in range(top, bottom+1):
            self.i = x
            yield self.matrix[x][self.j]
    
    def printUp(self, top, bottom):
        for x in range(bottom, top-1, -1):
            self.i = x
            yield self.matrix[x][self.j]
