class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        length_nums = len(nums)
        
        found_zero_at = 0
        
        for position in range(length_nums):
            if not nums[position] == 0:
                nums[position], nums[found_zero_at] = nums[found_zero_at], nums[position]
                found_zero_at+=1

        