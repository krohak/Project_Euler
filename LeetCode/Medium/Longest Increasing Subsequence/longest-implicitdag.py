class Solution(object):
    def lengthOfLIS(self, nums):
        if not nums:
            return 0

        L = [0 for num in nums]
        n = len(nums)

        for j in range(n):
            max_len = 0
            i = 0
            while i < n:
                if nums[i] < nums[j]  and L[i] > max_len:
                    max_len = L[i]
                i+=1

            L[j] = 1+max_len

        return max(L)


nums = [10,9,2,5,3,7,101,18]
sol = Solution().lengthOfLIS(nums)
print(sol)