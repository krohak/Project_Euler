from collections import deque

class Solution:
    def shortestSubarray(self, A, K):

        deq = deque()
        min_window = len(A)+1
        
        P = [0]
        for elem in A:
            P.append(P[-1]+elem)
        
        for i, elem in enumerate(P):
            
            while deq and P[deq[-1]] >= elem:
                deq.pop()
                
            while deq and (elem - P[deq[0]] >= K):   
                min_window = min(min_window, i-deq[0])
                deq.popleft()
            
            deq.append(i)
            
        
        return min_window if min_window < len(A)+1 else -1