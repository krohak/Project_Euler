class Solution:
    def increasingTriplet(self, nums) -> bool:
        
        maxIncreasingBefore = [0 for _ in range(len(nums))]
        
        for i in range(1, len(nums)):
            maxEdge = 0
            for j in range(i):
                if nums[i] > nums[j]: 
                    maxEdge = max(maxIncreasingBefore[j]+1, maxEdge)
            maxIncreasingBefore[i] = maxEdge
        return 2 in maxIncreasingBefore