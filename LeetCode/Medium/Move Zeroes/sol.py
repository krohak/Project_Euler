class Solution:
    def moveZeroes(self, nums):
        """
        Do not return anything, modify nums in-place instead.
        """
        
        length_nums = len(nums)
        
        position = 0
        non_zero = 0
        
        # find first zero 
        while(position < length_nums and not nums[position] == 0 ):
            position+=1
        
        # nothing to do
        if position == length_nums:
              return 
        
        
        non_zero = position + 1       
        
        while(non_zero < length_nums):
            
            if not nums[non_zero] == 0:
                nums[position] = nums[non_zero]
                nums[non_zero] = 0
                position+=1
            
            non_zero +=1
        
        return 