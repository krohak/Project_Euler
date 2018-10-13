def setMatrixZeroes(arr):

    row_bool = 1

    n = len(arr)
    m = len(arr[0])

    i = 0
    while i<n:
        if arr[i][0] == 0:
            row_bool = 0
        i+=1

    j = 0
    while j<m:
        if arr[0][j] == 0:
            arr[0][0] = 0
        j+=1

    i = 1
    while i<n:
        j = 1
        while j<m:

            if arr[i][j] == 0:
                arr[0][j] = 0
                arr[i][0] = 0

            j+=1
        i+=1

    if arr[0][0] == 0:
        j = 0
        while j<m:
            arr[0][j] = 0
            j+=1       
    
    if row_bool == 0:
        i = 0
        while i<n:
            arr[i][0] = 0
            i+=1

    return arr

arr = [
    [1,1,1,1],
    [1,0,0,1],
    [1,0,1,1],
    [1,1,1,1]
]

sol = setMatrixZeroes(arr)
print(sol)