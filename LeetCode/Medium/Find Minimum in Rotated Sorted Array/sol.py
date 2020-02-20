class Solution:
    def findMin(self, nums):
        
        n = len(nums)
        
        if not n:
            return -1
        if n==1:
            return nums[0]
        
        if n==2:
            return nums[0] if nums[0] < nums[1] else nums[1]
        
        left = 0 
        right = n-1
        
        first = nums[0]
        last = nums[n-1]
        
        while(left<=right):
            
            mid = (left+right)//2
                            
            if nums[(mid-1)%n] > nums[mid] and nums[(mid+1)%n] > nums[mid]:
                return nums[mid]
            
            elif first < nums[mid] and nums[mid]< last:
                right = mid - 1
                
            elif nums[mid] >= first and nums[mid] >= last:
                
                if first > last:
                    left = mid + 1
                    
                else:
                    right = mid -1
            
            elif nums[mid] < first and nums[mid] < last:
                
                if first > last:
                    right = mid - 1
                    
                else:
                    left = mid + 1
        
        return -1