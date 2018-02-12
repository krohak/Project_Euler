def permute(A,i):
    if i == len(A):
        print(A)
        return

    for j in range(i,len(A)):
        A[i], A[j] = A[j], A[i]
        permute(A, i+1)
        A[i], A[j] = A[j], A[i]

A = [1,2,3]
permute(A,0)
