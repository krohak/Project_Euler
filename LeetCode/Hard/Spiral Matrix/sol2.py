    def spiralOrder(self, matrix):
        
        m = len(matrix)
        if not m:
            return []
        n = len(matrix[0])
        if not n:
            return []
        
        row_start = 0
        row_end = m-1
        col_start = 0
        col_end = n-1
        
        answer = []
        
        while(row_start <= row_end and col_start <= col_end):
            
            for r,c in self.spiral_print(row_start, row_end, col_start, col_end):
                answer.append(matrix[r][c])
                
            row_start+=1
            row_end-=1
            col_start+=1
            col_end-=1
        
        return answer
            
    
    def spiral_print(self, row_start, row_end, col_start, col_end):
        
        for c in range(col_start, col_end+1):
            yield (row_start, c)
        
        for r in range(row_start+1, row_end+1):
            yield (r, col_end)
        
        if row_start < row_end and col_start < col_end:
            for c in range(col_end-1, col_start-1, -1):
                yield (row_end, c)

            for r in range(row_end-1, row_start, -1):
                yield (r, col_start)

