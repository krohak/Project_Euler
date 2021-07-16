class Solution:
    def searchRange(self, nums, target):
        left, right = 0, len(nums)-1
        
        while left < right:
            mid = (left+right)//2            
            if nums[mid] < target: left = mid + 1
            else: right = mid
        
        if (not nums or nums[left]!=target): return [-1, -1]
    
        start, right = left, len(nums)-1
        while left < right:
            mid = ((left+right)//2)+1            
            if nums[mid] > target:
                right = mid - 1
            else: left = mid
        
        return [start, right]