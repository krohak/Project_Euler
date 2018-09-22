import bisect
class Solution(object):
    def lengthOfLIS(self, nums):

        dp = [0 for num in nums]
        
        end_dp = 0

        for num in nums:
            i = bisect.bisect_left(dp, num, 0, end_dp)
            
            dp[i] = num

            if i == end_dp:
                end_dp+=1

        return end_dp


nums = [10,9,2,5,3,7,101,18]
sol = Solution().lengthOfLIS(nums)
print(sol)