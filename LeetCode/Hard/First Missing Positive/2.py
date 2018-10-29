class Solution(object):
    def firstMissingPositive(self, nums):

        n = len(nums)
        if n == 0:
            return 1
        
        # increase length, make first index 1
        nums.append(-1)

        # first pass, three cases
        for i in range(n):
            
            if nums[i] == i:
                continue

            # out of upper bound 
            if nums[i] > n:
                continue
            
            # out of lower bound
            elif nums[i] < 0:
                continue
            
            # exchange
            else:
                temp = nums[nums[i]]

                # is temp in the right place?
                if temp == nums[i]:
                    nums[i] = -1
                
                else:
                    nums[nums[i]] = nums[i]
                    nums[i] = temp

        print(nums)

        # second pass, return FMP
        for i in range(1,n+1):
            
            if not nums[i] == i:
                return i
        
        return n


nums = [-1,4,2,1,9,10]
# print(nums)
nums = [3,4,-1,1]
sol = Solution().firstMissingPositive(nums)
print(sol)