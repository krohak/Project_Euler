answer=[] 
count = 0

def printForward(arr,i,j,col_end):
    global count
    answer.append(arr[i][j])
    count+=1
    while(j<col_end):
        j+=1
        count+=1
        answer.append (arr[i][j])
    return j

def printBackward(arr,i,j,col_start):
    global count
    answer.append(arr[i][j])
    count+=1
    while(j>col_start):
        j-=1
        count+=1
        answer.append(arr[i][j])
    return j


def printDown (arr,i,j,row_end):
    global count
    answer.append(arr[i][j])
    count+=1
    while(i<row_end):
        i+=1
        count+=1
        answer.append(arr[i][j])
    return i


def printUp(arr,i,j,row_start):
    global count
    answer.append(arr[i][j])
    count+=1
    while(i>row_start):
        i-=1
        count+=1
        answer.append(arr[i][j])
    return i


class Solution(object):
    def spiralOrder(self, arr):
        
        global answer
        answer=[] 
        global count
        count = 0

        n_row = len(arr)
    
        if n_row == 0:
            return []

        n_col = len(arr[0])     
        if n_row == 1:
            printForward(arr,0,0,n_col-1)
            return answer
        
        # row_center = n_row // 2
        # col_center = n_col // 2
        
        row_end = n_row-1
        row_start = 0
        col_end = n_col-1
        col_start = 0
        
        i,j = 0,0
        n = n_row*n_col

        while (not count >= n):
            
            j = printForward(arr,i,j,col_end)
            if (count >= n):
                break
            row_start+=1
            i=row_start
            
            
            i = printDown(arr,i,j,row_end)
            if (count >= n):
                break
            col_end-=1
            j=col_end
           
            
            j = printBackward(arr,i,j,col_start)
            if (count >= n):
                break
            row_end-=1
            i=row_end
           
            
            i = printUp(arr,i,j,row_start)
            if (count >= n):
                break
            col_start+=1
            j=col_start
        
        return answer


arr = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

solObj = Solution()

answer = solObj.spiralOrder(arr)
print(answer)