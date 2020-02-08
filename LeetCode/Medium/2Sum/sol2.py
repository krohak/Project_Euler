from collections import Counter

class Solution:
    def twoSum(self, nums, target):
        
        indices = {}
        
        for index, number in enumerate(nums):
        
            if ( (target-number) in indices):
                return [index, indices[target-number]]        

            indices[number] = index
        
        return []
            