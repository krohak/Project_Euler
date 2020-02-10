class Solution:
    def maxProduct(self, nums):
        if len(nums) == 0:
            return 0

        ans = nums[0]

        max_prod, min_prod = 1, 1
        
        for elem in nums:

            max_prod, min_prod = max(elem, elem*max_prod, elem*min_prod), min(elem, elem*max_prod, elem*min_prod)
            ans = max(ans, max_prod)

        return ans