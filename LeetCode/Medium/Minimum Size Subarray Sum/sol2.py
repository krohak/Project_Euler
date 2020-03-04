
from collections import deque

class Solution:
    def minSubArrayLen(self, s, nums):
        
        n = len(nums)
        
        window_start = 0
        window_size = 0
        window_sum = 0
        
        min_size = float('inf')
        
        window_end = 0
        while window_end < n:

            num=nums[window_end]
            
            if window_sum+num >= s:
                                
                min_size = min(min_size, window_size+1)
                
                window_sum-=nums[window_start]
                window_start+=1
                window_size-=1
                continue
            
            else:
                window_sum+=num
                window_size+=1
                window_end+=1
        
        return min_size if not min_size == float('inf') else 0