def set_matrix_zeroes(arr):

    m = len(arr)
    n = len(arr[0])

    print(m, n)

    row_zero = 0
    col_zero = 0

    i = 0
    while i<m:
        if arr[i][0] == 0:
            col_zero = 1
        i+=1
    
    j = 0
    while j<n:
        if arr[0][j] == 0:
            row_zero = 1
        j+=1

    # print(row_zero, col_zero)

    i = 1
    # print(i, j)
    while i<m:
        j = 1
        while j<n:
            # print(i, j, arr[i][j])
            if arr[i][j] == 0:
                
                arr[i][0] = 0
                arr[0][j] = 0

            j+=1
        i+=1
    
    # print(i, j, arr)

    i, j = 1, 1
    # make rows zero
    while i<m:
        if arr[i][0] == 0:
            arr[i] = [0]*n
        i+=1
    
    # make col zero
    while j<n:
        if arr[0][j] == 0:

            k = 0
            while k<m:
                arr[k][j] = 0
                k+=1

        j+=1
    
    if col_zero:
        k = 0
        while k<m:
            arr[k][0] = 0
            k+=1

    if row_zero:
        arr[0] = [0]*n

    return arr

arr = [
    [1,1,1,1],
    [1,0,0,1],
    [1,0,1,1],
    [1,1,1,1]
]


arr = [
  [1,1,1],
  [1,0,1],
  [1,1,1]
]

arr = [
  [0,1,2,0],
  [3,4,5,2],
  [1,3,1,5]
]


arr = [
    [1,2,3,4],
    [5,0,5,2],
    [8,9,2,0],
    [5,7,2,1]
]


sol = set_matrix_zeroes(arr)
print(sol)