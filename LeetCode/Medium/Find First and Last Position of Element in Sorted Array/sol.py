class Solution:
    def searchRange(self, nums, target):       
        start = self.bisect(nums, target)
        if (start == len(nums) or nums[start]!=target): return [-1, -1]
        end = self.bisect(nums, target+1) - 1
        return [start, end]
    
    def bisect(self, nums, target):
        left, right = 0, len(nums)
        while left < right:
            mid = (left+right)//2            
            if nums[mid] < target: left = mid + 1
            else: right = mid     
        return left