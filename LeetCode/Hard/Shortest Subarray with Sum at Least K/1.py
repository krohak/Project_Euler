from collections import deque

class Solution:
    def shortestSubarray(self, A, K):
        
        n = len(A)
        running_sum = 0
        deq = deque()
        len_deq = 0
        
        min_len = float('inf')
        
        i = 0
        while i<n:
            
            while i<n and running_sum < K:
                deq.append(A[i])
                running_sum+=A[i]
                i+=1
                len_deq+=1
            
            while deq and running_sum >= K:
                min_len = min(min_len, len_deq)
                elem_left = deq.popleft()
                running_sum-=elem_left
                len_deq-=1
        
        return min_len if not min_len == float('inf') else -1
        
        