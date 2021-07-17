import heapq

def heapSort(arr):
    heapq.heapify(arr)
    ans = []
    while arr:
        elem = heapq.heappop(arr)
        ans.append(elem)
    return ans

import numpy as np
for k in range(1):
    n=100
    randomList = np.random.rand(100)*100
    print(randomList)
    randomList = heapSort(list(randomList))
    print(randomList)
    print(all(randomList[i] <= randomList[i+1] for i in range(len(randomList)-1)))