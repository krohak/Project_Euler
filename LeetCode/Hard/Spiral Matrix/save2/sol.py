class Solution:
    
    def __init__(self):
        self.count = 0

    def spiralOrder(self, matrix):
        
        self.m = len(matrix)
        if not self.m:
            return []
        
        self.n = len(matrix[0])
        if not self.n:
            return []
        
        answer = []
        
        row_start, row_end = 0, self.m-1
        col_start, col_end = 0, self.n-1
        
        cells = self.m*self.n
        
        while self.count < cells:
            
            for (r,c) in self.spiral_layer(row_start, row_end, col_start, col_end):             
                answer.append(matrix[r][c])

            row_start +=1 
            row_end -=1
            col_start +=1
            col_end -=1
    
        return answer
    
    def spiral_layer(self, row_start, row_end, col_start, col_end):
            
        for c in range(col_start, col_end+1):
            self.count+=1
            yield (row_start, c)
            
        for r in range(row_start+1, row_end+1):
            self.count+=1
            yield (r, col_end)

        if row_start < row_end and col_start < col_end:
            
            for c in reversed(range(col_start, col_end)):
                self.count+=1
                yield (row_end, c)
                
            for r in reversed(range(row_start+1, row_end)):
                self.count+=1
                yield(r, col_start)


arr = [
    [1,2,3,4],
    [5,6,7,8],
    [9,10,11,12],
    [13,14,15,16]
]

arr = [[1,2,3],[4,5,6],[7,8,9]]

arr = [
        [1,2,3,4],
        [5,6,7,8],
        [9,10,11,12]
]


arr = [[3],[2]]

solObj = Solution()

answer = solObj.spiralOrder(arr)
print(answer)