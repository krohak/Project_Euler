class Solution(object):
    def maximumProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        nums.sort()
        
        first_element = nums[0]
        second_element = nums[1]

        last_element = nums[-1]
        second_last_element = nums[-2]
        third_last_element = nums[-3]

        positive_nums_product = last_element*second_last_element*third_last_element
        negative_nums_product = first_element*second_element*last_element

        return max(positive_nums_product, negative_nums_product)