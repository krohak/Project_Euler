class Solution:
    def findDuplicate(self, nums):
        slow = fast = nums[0]
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break
        ref = nums[0]
        cycle_count = 0 
        while ref != slow:
            ref = nums[ref]
            cycle_count+=1
        slow = nums[0]
        while cycle_count>0:
            slow = nums[slow]
            cycle_count-=1
        ref = nums[0]
        while ref != slow:
            ref = nums[ref]
            slow = nums[slow]
        return ref


arr = [1,3,4,2,2]
# arr = [3,1,3,4,2]
dup = Solution().findDuplicate(arr)
print(dup)