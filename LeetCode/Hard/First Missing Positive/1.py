class Solution(object):
    def firstMissingPositive(self, nums):
        

        # first pass, three cases
        n = len(nums)

        if n == 0:
            return 1

        for i in range(n):

            # out of upper bound 
            if nums[i] >= n:
                continue
            
            # out of lower bound
            elif nums[i] < 0:
                continue
            
            # exchange
            else:
                temp = nums[nums[i]-1]
                nums[nums[i]-1] = nums[i]
                nums[i] = temp
                print(nums)
                while nums[i] >= n or nums[i] < 0 :
                    temp = nums[nums[i]-1]
                    nums[nums[i]-1] = nums[i]
                    nums[i] = temp
                    print(nums)

        print(nums)

        # second pass, return FMP
        for i in range(n):
            
            if not nums[i] == i+1:
                return i+1
        
        return n+1


nums = [-1,4,2,1,9,10]
print(nums)
sol = Solution().firstMissingPositive(nums)