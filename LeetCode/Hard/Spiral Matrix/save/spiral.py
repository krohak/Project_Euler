answer=[] 

def printForward(arr,i,j,col_end):
    while(j<col_end):
        answer.append (arr[i][j])
        j+=1
    answer.append(arr[i][j])
    return j

def printBackward(arr,i,j,col_start):
    while(j>col_start):
        answer.append(arr[i][j])
        j-=1
    answer.append(arr[i][j])
    return j


def printDown (arr,i,j,row_end):
    while(i<row_end):
        answer.append(arr[i][j])
        i+=1
    answer.append(arr[i][j])
    return i


def printUp(arr,i,j,row_start):
    while(i>row_start):
        answer.append(arr[i][j])
        i-=1
    answer.append(arr[i][j])
    return i


class Solution(object):
    def spiralOrder(self, arr):
        
        global answer
        answer=[] 

        n_row = len(arr)
        n_col = len(arr[0]) 
        
        row_center = n_row // 2
        col_center = n_col // 2
        
        row_end = n_row-1
        row_start = 0
        col_end = n_col-1
        col_start = 0
        
        i,j = 0,0
        
        while (not i == row_center or not j == col_center):
            
            j = printForward(arr,i,j,col_end)
            if (i == row_center and j == col_center):
                break
            row_start+=1
            i=row_start
            
            
            i = printDown(arr,i,j,row_end)
            if (i == row_center and j == col_center):
                break
            col_end-=1
            j=col_end
           
            
            j = printBackward(arr,i,j,col_start)
            if (i == row_center and j == col_center):
                break
            row_end-=1
            i=row_end
           
            
            i = printUp(arr,i,j,row_start)
            if (i == row_center and j == col_center):
                break
            col_start+=1
            j=col_start
        
        
        return answer


