
from collections import deque

class Solution:
    def minSubArrayLen(self, s, nums):
        
        n = len(nums)
        
        window_start = 0
        window_size = 0
        window_sum = 0
        
        min_size = float('inf')
        
        
        for num in nums:
            
            if window_sum+num >= s:
                window_sum+=num
                window_size+=1
                min_size = min(min_size, window_size)
                
                while(window_start < n and window_sum>=s):
                    window_sum-=nums[window_start]
                    window_start+=1
                    window_size-=1
                    if window_sum>=s:
                        min_size = min(min_size, window_size)
            
            else:
                window_sum+=num
                window_size+=1
        
        return min_size if not min_size == float('inf') else 0