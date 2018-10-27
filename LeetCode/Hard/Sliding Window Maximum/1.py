class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        pass


    

def preCompute(nums, k):

    compute = []

    n = len(nums)
    i = k

    while i<n:

        if nums[i] > nums[i-k]:
            compute.append(nums[i])
        else:
            compute.append(nums[i-k])
        i+=1

    return compute



nums = [1,3,-1,-3,5,3,6,7]
k = 3

comp = preCompute(nums, k)
print(comp)