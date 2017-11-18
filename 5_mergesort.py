import numpy as np

nums=np.random.random(10)*100//1
nums=nums.tolist()

def MergeSort(arr):
    length = len(arr)

    if length == 1:
        return

    l1=length//2
    l2=length-l1
    A = arr[:l1]
    B = arr[l1:]

    #print(A,B)

    MergeSort(A)
    MergeSort(B)

    countA=0
    countB=0
    i=0

    while (countA<l1 and countB<l2):
        if A[countA]<=B[countB]:
            arr[i]=A[countA]
            countA+=1
            i+=1

        else:
            arr[i]=B[countB]
            countB+=1
            i+=1

    while (countA<l1):
        arr[i] = A[countA]
        countA+=1
        i+=1

    while(countB<l2):
        arr[i] = B[countB]
        countB+=1
        i+=1

    #print(arr)
    #return ans


if __name__ == "__main__":
    t = int(input().strip())
    for a0 in range(t):
        n = int(input().strip())
        arr = list(map(int, input().strip().split(' ')))
        print(nums)
        MergeSort(nums)
        print(nums)
