class Solution(object):
    def findDuplicate(self, nums):
        
        # form cycle so that duplicate is at start
        slow = nums[0]
        fast = nums[nums[0]]

        while slow != fast:
            slow = nums[slow]
            fast = nums[nums[fast]]

        # get length of cycle
        ref = nums[slow]
        count = 1
        while ref != slow:
            ref = nums[ref]
            count+=1
        
        # print cycle start point
        slow = nums[0]
        while count>0:
            slow = nums[slow]
            count-=1

        ref = nums[0]
        while ref != slow:
            ref = nums[ref]
            slow = nums[slow]
        
        return ref


nums = [1,3,4,2,2]
sol = Solution().findDuplicate(nums)
print(sol)