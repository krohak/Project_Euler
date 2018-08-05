class Solution:
    def longestConsecutive(self, nums):
        
        num_set = set(nums)
        max_cons = 0
        for num in num_set:
            if num-1 not in num_set:
                prev_num = num
                cons = 1

                while prev_num + 1 in num_set:
                    prev_num += 1
                    cons += 1

                max_cons = max(max_cons, cons)
        
        return max_cons



arr = [1,2,3]
solobj = Solution()
cons = solobj.longestConsecutive(arr)
print(cons)