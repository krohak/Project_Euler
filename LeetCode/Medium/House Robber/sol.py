class Solution:
    def rob(self, nums):
        
        if not nums:
            return 0
    
        dp = [ num for num in nums ]
        
        n = len(nums)
        
        for house in range(1, n):
            
            for neighbour in range(house-1):
                
                dp[house] = max(dp[house], dp[neighbour]+nums[house])
        
        return max(dp)