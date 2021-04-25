from collections import Counter

class Solution:
    def twoSum(self, nums, target):
        
        
        freq_counter = Counter(nums)
        
        indices = {}
        
        for index, number in enumerate(nums):
            indices[number] = index
        
        
        for index, number in enumerate(nums):
            
            freq_counter[number] -=1
            
            if (freq_counter[(target-number)] > 0):
                return [index, indices[target-number]]
            
            freq_counter[number] +=1
            
        
        return []
            