class Solution:
    def subarraySum(self, nums, target_sum):

        counter = 0

        sum_dict = {0:1}
        
        current_sum = 0

        for i in range(0, len(nums)):
            current_sum += nums[i]

            if (current_sum-target_sum) in sum_dict:
                counter+=sum_dict[current_sum-target_sum]

            if current_sum in sum_dict:
                sum_dict[current_sum]+=1
            else:
                sum_dict[current_sum]=1

        return counter


nums = [1,1,1,1,2,2,1,1]
sol = Solution().subarraySum(nums, 2)

print(sol)