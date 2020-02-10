class Solution(object):
    def maximumProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 
        if len(nums) < 3:
            return
        
        if len(nums) == 3:
            return nums[0]*nums[1]*nums[2]
        
        nums.sort()
        
        first_element = nums[0]
        last_element = nums[-1]
        
        if first_element < 0 and last_element > 0:
            
            second_element = nums[1]
            
            second_last_element = nums[-2]
            third_last_element = nums[-3]
            
            positive_nums_product = last_element*second_last_element*third_last_element
            negative_nums_product = first_element*second_element*last_element
            
            return max(positive_nums_product, negative_nums_product)
        
        elif last_element == 0:
            return 0
        
        else:
            second_last_element = nums[-2]
            third_last_element = nums[-3]
            
            nums_product = last_element*second_last_element*third_last_element
            return nums_product
            