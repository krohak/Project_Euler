import heapq

def heapSort(arr):
    heapq.heapify(arr)
    n = len(arr)
    return [ heapq.heappop(arr) for _ in range(n) ]

import numpy as np
for k in range(1):
    n=100
    randomList = np.random.rand(100)*100
    print(randomList)
    randomList = heapSort(list(randomList))
    print(randomList)
    print(all(randomList[i] <= randomList[i+1] for i in range(len(randomList)-1)))