def permute(A,j):
    if j == len(A):
        print(A)
        return

    for i in range(j,len(A)):
        A[j], A[i] = A[i], A[j]
        permute(A, j+1)
        A[j], A[i] = A[i], A[j]

A = [1,2,3]
permute(A,0)
