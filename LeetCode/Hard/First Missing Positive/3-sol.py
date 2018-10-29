class Solution(object):
    def firstMissingPositive(self, nums):

        n = len(nums)
        if n == 0:
            return 1
        
        # increase length, make first index 1
        nums.append(-1)

        # first pass, three cases
        i = 0
        while i<n:
            
            if nums[i] == i:
                i+=1

            # out of upper bound 
            elif nums[i] > n:
                i+=1
            
            # out of lower bound
            elif nums[i] < 0:
                i+=1
            
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
        
        return n+1


nums = [-1,4,2,1,9,10]
# print(nums)
nums = [3,4,-1,1]
sol = Solution().firstMissingPositive(nums)
print(sol)