def goRight(i, j, arr, stop_j, ans, count):    
    while j<stop_j:
        ans.append(arr[i][j])
        j+=1
        count+=1
    return j-1, ans, count

def goLeft(i, j, arr, stop_j, ans, count):    
    while j>=stop_j:
        ans.append(arr[i][j])
        j-=1
        count+=1
    return j+1, ans, count

def goDown(i, j, arr, stop_i, ans, count):    
    while i<stop_i:
        ans.append(arr[i][j])
        i+=1
        count+=1
    return i-1, ans, count

def goUp(i, j, arr, stop_i, ans, count):    
    while i>stop_i:
        ans.append(arr[i][j])
        i-=1
        count+=1
    return i+1, ans, count

class Solution(object):
    def spiralOrder(self, arr):

        n = len(arr)
        
        if n == 0:
            return []
        
        m = len(arr[0])

        if m == 0:
            return []
        
        col_start = row_start = 0
        row_end = n
        col_end = m

        total = n*m
        
        count = 1
        i = j = 0
        ans = []

        ans.append(arr[0][0])

        while count < total:

            j, ans, count = goRight(i, j+1, arr, col_end, ans, count)

            if count >= total:
                break

            i, ans, count = goDown(i+1, j, arr, row_end, ans, count)

            if count >= total:
                break

            j, ans, count = goLeft(i, j-1, arr, col_start, ans, count)

            if count >= total:
                break

            i, ans, count = goUp(i-1, j, arr, row_start, ans, count)

            if count >= total:
                break

            col_start+=1
            row_start+=1
            col_end-=1
            row_end-=1

            # print(ans, count, total)
        return ans
arr = [
    [1,2,3,4],
    [5,6,7,8],
    [9,10,11,12],
    [13,14,15,16]
]

solObj = Solution()

answer = solObj.spiralOrder(arr)
print(answer)