class Solution:
    def subarraySum(self, nums, target_sum):
        
        cumulative_sum = {0:1}
        
        counter = 0
        
        summ = 0
        for num in nums:
            summ+=num
            
            if (summ-target_sum) in cumulative_sum:
                counter+=cumulative_sum[(summ-target_sum)]
            
            cumulative_sum[summ] = cumulative_sum.get(summ, 0)+1
            
        return counter


nums = [1,1,1,1,2,2,1,1]
sol = Solution().subarraySum(nums, 2)

print(sol)