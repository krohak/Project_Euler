import heapq

def heap_sort(arr):

    heapq.heapify(arr)

    ans = []
    while arr:
        elem = heapq.heappop(arr)
        ans.append(elem)

    return ans


arr = [3,6,10,2,7,4,5,9,1,8,3,6,10,2,7,4,5,9,1,8]
ans = heap_sort(arr)
print(ans)