class Solution:
    def increasingTriplet(self, nums) -> bool:
        
        nodeZero = nums[0]
        nodeOne = float('inf')
        
        for i in range(1, len(nums)):
            if nums[i] > nodeOne:
                return True
            if nums[i] > nodeZero:
                nodeOne = min(nums[i], nodeOne)
            nodeZero = min(nums[i], nodeZero)
        return False
            