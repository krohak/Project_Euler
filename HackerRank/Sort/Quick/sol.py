def callQuickSort(arr):
    quickSort(arr, 0, len(arr)-1)
    return arr

def quickSort(arr, left, right):
    if left >= right: return
    arr, pivotI = sortAroundPivot(arr, left, right)
    quickSort(arr, left, pivotI-1)
    quickSort(arr, pivotI+1, right)
    

def sortAroundPivot(arr, left, right):
    pivot = arr[left]
    i, j, x = left, right, left+1
    while i < j:
        if arr[x] <= pivot:
            arr[x], arr[i] = arr[i], arr[x]; i+=1; x+=1
        else:
            arr[x], arr[j] = arr[j], arr[x]; j-=1
    arr[i] = pivot
    return arr, i

import numpy as np
for k in range(1):
    n=100
    randomList = np.random.rand(100)*100
    print(randomList)
    randomList = callQuickSort(randomList)
    print(randomList)
    print(all(randomList[i] <= randomList[i+1] for i in range(len(randomList)-1)))