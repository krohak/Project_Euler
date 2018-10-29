class Solution(object):
    def maxProduct(self, nums):
        
        n = len(nums)

        L_low = [0 for i in range(n)]
        L_high = [0 for i in range(n)]

        L_high[0] = nums[0]
        L_low[0] = nums[0]

        ans = nums[0]

        i = 1
        while i<n:
                    
            L_low[i] = min( nums[i]*L_low[i-1], nums[i]*L_high[i-1], nums[i] )
            L_high[i] = max( nums[i]*L_low[i-1], nums[i]*L_high[i-1], nums[i] )

            ans = max(ans, L_high[i], L_low[i] )
            i+=1

        return ans



nums = [2,3,-2,4]
sol = Solution().maxProduct(nums)
print(sol)