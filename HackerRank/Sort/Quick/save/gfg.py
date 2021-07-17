def partition(arr, low, high):
    i = (low-1)         # index of smaller element
    pivot = arr[high]     # pivot
    for j in range(low, high):
        if arr[j] <= pivot:
            i = i+1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i+1], arr[high] = arr[high], arr[i+1]
    return (i+1)
  
  
def quickSort(arr, low, high):
    if len(arr) == 1:
        return arr
    if low < high:
        pi = partition(arr, low, high)
        quickSort(arr, low, pi-1)
        quickSort(arr, pi+1, high)
    return arr

import numpy as np
for k in range(1):
    n=100
    randomList = np.random.rand(100)*100
    print(randomList)
    randomList = quickSort(randomList, 0, len(randomList)-1)
    print(randomList)
    print(all(randomList[i] <= randomList[i+1] for i in range(len(randomList)-1)))