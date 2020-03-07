class Solution:
    def findUnsortedSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        
        left = n
        right = 0
        
        stack = []
        
        for i in range(n):
            
            num = nums[i]
            while stack and nums[stack[-1]] > num:
                left = min(left, stack.pop())
            
            stack.append(i)
        
        
        stack = []
        for i in reversed(range(n)):
            
            num = nums[i]
            while stack and nums[stack[-1]] < num:
                right = max(right, stack.pop())
            
            stack.append(i)
        
        return right-left+1 if right>left else 0