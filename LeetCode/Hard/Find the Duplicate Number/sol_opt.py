class Solution:
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        slow = fast = nums[0]
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break
        temp = nums[0]
        while temp != slow:
            temp = nums[temp]
            slow = nums[slow]
        return temp


arr = [1,3,4,2,2]
# arr = [3,1,3,4,2]
dup = Solution().findDuplicate(arr)
print(dup)