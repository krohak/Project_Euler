class Solution:
    def longestConsecutive(self, nums):

        num_set = set(nums)

        max_cons = 0

        for num in nums:

            if num-1 not in num_set:

                cons = 0
                i = num
                while i in num_set:
                    cons+=1
                    i+=1
                
                max_cons = max(max_cons, cons)
        
        return max_cons


arr = [1,2,3]
cons = Solution().longestConsecutive(arr)
print(cons)