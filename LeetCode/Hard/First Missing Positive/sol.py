class Solution:
    
    def firstMissingPositive(self,nums):
        size = len(nums)
        i = 0
        nums.append(-1)
        while (i<size):
            # if num at correct index, negative or greater then size of array
            if nums[i] == i or nums[i] < 0 or nums[i] > size: 
                i+=1
            else:
                if nums[nums[i]] == nums[i]: # nums[nums[3]] == nums[5] ?
                    nums[i] = -1 # mark
                else:
                    tmp = nums[nums[i]] # nums[5] is x
                    nums[nums[i]] = nums[i] # nums[5] = nums[3]
                    nums[i] = tmp # nums[3] = x
        i = 1
        while (i<=size):
            if nums[i] != i:
                return i
            i+=1
        return i

