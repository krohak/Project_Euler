class Solution(object):
    def spiralOrder(self, matrix):
        m = len(matrix)
        if not m: return []
        n = len(matrix[0])
        if not n: return matrix
        self.matrix = matrix
        self.cursor = (0,0)
        rightLimit, downLimit, leftLimit, upLimit = n-1, m-1, 0, 0
        spiral = []
        while rightLimit >= leftLimit and downLimit >= upLimit:
            spiral.extend(self.printRight(rightLimit))
            upLimit+=1
            spiral.extend(self.printDown(downLimit))
            rightLimit-=1
            if rightLimit >= leftLimit and downLimit >= upLimit:
                spiral.extend(self.printLeft(leftLimit))
                downLimit-=1
                spiral.extend(self.printUp(upLimit))
                leftLimit+=1
        return spiral

    def printRight(self, rightLimit):
        x,y = self.cursor
        self.cursor = (x, rightLimit)
        return [ self.matrix[x][y1] for y1 in range(y, rightLimit+1) ]

    def printDown(self, downLimit):
        x,y = self.cursor
        self.cursor = (downLimit, y)
        return [ self.matrix[x1][y] for x1 in range(x+1, downLimit+1) ]

    def printLeft(self, leftLimit):
        x,y = self.cursor
        self.cursor = (x, leftLimit)
        return [ self.matrix[x][y1] for y1 in range(y-1, leftLimit-1, -1) ]

    def printUp(self, upLimit):
        x,y = self.cursor
        self.cursor = (upLimit, y+1)
        return [  self.matrix[x1][y] for x1 in range(x-1, upLimit-1, -1) ]

matrix = [[1,2,3],[4,5,6],[7,8,9]]
matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
print(Solution().spiralOrder(matrix))