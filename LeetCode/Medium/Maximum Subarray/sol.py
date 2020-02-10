class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        L = [ num for num in nums ]
        
        
        for i in range(1, len(nums)):
            
            L[i] = max( L[i-1]+L[i], L[i])
        
        
        return max(L)