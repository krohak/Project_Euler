answer=[] 

def printForward(arr,i,j,col_end):
    answer.append(arr[i][j])
    while(j<col_end):
        j+=1
        answer.append (arr[i][j])
    return j

def printBackward(arr,i,j,col_start):
    answer.append(arr[i][j])
    while(j>col_start):
        j-=1
        answer.append(arr[i][j])
    return j


def printDown (arr,i,j,row_end):
    answer.append(arr[i][j])
    while(i<row_end):
        i+=1
        answer.append(arr[i][j])
    return i


def printUp(arr,i,j,row_start):
    answer.append(arr[i][j])
    while(i>row_start):
        i-=1
        answer.append(arr[i][j])
    return i


class Solution(object):
    def spiralOrder(self, arr):
        
        global answer
        answer=[] 

        n_row = len(arr)
    
        if n_row == 0:
            return []

        n_col = len(arr[0])     
        if n_row == 1:
            printForward(arr,0,0,n_col-1)
            return answer
                
        row_end = n_row-1
        row_start = 0
        col_end = n_col-1
        col_start = 0
        
        i,j = 0,0

        while (row_start <= row_end and col_start<=col_end):
            
            j = printForward(arr,i,j,col_end)
            row_start+=1
            i=row_start
            if (row_start > row_end):
                break
            
            i = printDown(arr,i,j,row_end)
            col_end-=1
            j=col_end
            if (col_start > col_end):
                break
            
            j = printBackward(arr,i,j,col_start)
            row_end-=1
            i=row_end
            if (row_start > row_end):
                break
            
            i = printUp(arr,i,j,row_start)
            col_start+=1
            j=col_start
            if (col_start > col_end):
                break

        return answer


# arr = [
#     [1,2,3],
#     [4,5,6],
#     [7,8,9]
# ]

arr = [
    [1,2,3,4],
    [5,6,7,8],
    [9,10,11,12],
    [13,14,15,16]
]

solObj = Solution()

answer = solObj.spiralOrder(arr)
print(answer)