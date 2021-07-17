def mergeSort(arr):

    lenArr = len(arr)
    if lenArr==1:
        return arr

    leftHalf = mergeSort(arr[:lenArr//2])
    rightHalf = mergeSort(arr[lenArr//2:])

    merged = []
    i, j = 0, 0
    while i<len(leftHalf) and j<len(rightHalf):
        elem, i, j = min((leftHalf[i], i+1, j), (rightHalf[j], i, j+1))
        merged.append(elem)
    while i<len(leftHalf):
        merged.append(leftHalf[i]); i+=1
    while j<len(rightHalf):
        merged.append(rightHalf[j]); j+=1
    return merged

import numpy as np
for k in range(1):
    n=100
    randomList = np.random.rand(100)*100
    print(randomList)
    randomList = mergeSort(randomList)
    print(randomList)
    print(all(randomList[i] <= randomList[i+1] for i in range(len(randomList)-1)))