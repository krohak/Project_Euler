class Solution:
    def search(self, nums, target):
        
        left = 0
        right = len(nums)-1
        
        while(left<=right):
            
            mid = (left+right)//2
            
            if nums[mid] == target:
                return True
            
            elif nums[left] == nums[mid]:
                left+=1
            
            elif nums[right] == nums[mid]:
                right-=1
            
            elif nums[left] <= nums[mid]:
                if nums[left] <= target and target < nums[mid]:
                    right = mid - 1 
                else:
                    left = mid + 1
                
            elif nums[left] > nums[mid]:
                if nums[right] >= target and nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1
        
        return False