class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maxArr = [ None for _ in range(len(nums)) ]
        maxArr[0] = nums[0]
        for i in range(1, len(nums)):
            maxArr[i] = max(maxArr[i-1]+nums[i], nums[i])
        return max(maxArr)