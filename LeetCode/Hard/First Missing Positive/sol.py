class Solution:
    def firstMissingPositive(self, nums):

        if len(nums) == 0:
            return 1

        if len(nums) == 2:

            if (nums[0] > 0 or nums[1] > 0) and nums[0]*nums[1] == 0:
                return 2
            elif nums[0] > 0 and nums[0]*nums[1] == 2:
                return 3
            elif nums[0] == 1 or nums[1] == 1:
                return min(nums[0],nums[1])+1
            else:
                return 1

        pointer = nums.pop(0)
        least = pointer

        for elem in nums:
            if elem < least and least - elem == 1:
                least = elem

            if elem == pointer+1:
                pointer = elem
            elif elem < pointer and not pointer - elem == 1 and not elem == least:
                pointer = elem



        print(least, pointer)

        if least > 1:
            return 1

        if pointer <= 0:
            return 1

        return pointer+1 
