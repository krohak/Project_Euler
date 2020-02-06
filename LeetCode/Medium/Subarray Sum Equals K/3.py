class Solution:
    def subarraySum(self, nums, target_sum):

        counter = 0

        sums = [ 0 for x in range(len(nums)+1) ]

        for i in range(1, len(nums)+1):
            sums[i] = sums[i-1] + nums[i-1]

        
        for start in range(0, len(nums)):
            for end in range(start+1, len(nums)+1):
                if (sums[end] - sums[start] == target_sum):
                    counter+=1

        return counter
                    

nums = [1,1,1,1,2,2,1,1]
sol = Solution().subarraySum(nums, 2)

print(sol)