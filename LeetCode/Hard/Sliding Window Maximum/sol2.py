from collections import deque 

class Solution(object):
    
    
    def __init__(self):
        self.deq = deque()
        self.k = 0
        self.nums = []
    
    def maxSlidingWindow(self, nums, k):
        
        n = len(nums)
        
        if not k*n:
            return 
        
        if k==1:
            return nums
        
        self.k = k
        self.nums = nums
        
        ans = []
        
        self.deq.append(0)
        for i in range(1, k):
            self.clean(i)
            self.deq.append(i)
            
        ans.append(self.nums[self.deq[0]]) 
        
        for i in range(k, n):
            self.clean(i)
            self.deq.append(i)
            ans.append(self.nums[self.deq[0]]) 
    
        return ans
    
    
    def clean(self, i):
        
        if self.deq and self.deq[0] <= i-self.k:
            self.deq.popleft()
        
        
        while self.deq and self.nums[self.deq[-1]] < self.nums[i]:
            self.deq.pop()
        
    
        