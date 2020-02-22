import heapq

def sort_k_messed_array(arr, k):
  
  if not k:
    return arr
  
  heap = [ arr[i] for i in range(k+1) ]
  heapq.heapify(heap)
  
  ans = []
  
  n = len(arr)
  for i in range(k+1, n):
    
    min_element = heapq.heappop(heap)
    ans.append(min_element)
    heapq.heappush(heap, arr[i])
  
  while heap:
    ans.append(heapq.heappop(heap))
  
  return ans
