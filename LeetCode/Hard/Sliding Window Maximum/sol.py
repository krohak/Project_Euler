from collections import deque
idxi, numi = 0, 1

class Solution:
    def maxSlidingWindow(self, nums: list, k: int) -> list:
        
        window = deque([])
        
        for i in range(k):
            while window and nums[i] > window[-1][numi]:
                window.pop()
            window.append((i, nums[i]))
                 
        answer = [window[0][numi]]
            
        i = k
        while i < len(nums):
            while window and nums[i] >= window[-1][numi]:
                window.pop()
            window.append((i, nums[i]))
            
            while window and window[0][idxi] < i-k+1:
                window.popleft()
            answer.append(window[0][numi])
            i+=1
        
        return answer