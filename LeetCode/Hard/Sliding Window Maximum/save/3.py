from collections import deque 

def getHighestFirstK(deq, nums, k):

    i = 0
    while i<k:


        # if new greater, flush deq
        if nums[i] > nums[deq[0]]:
            while deq: 
                deq.popleft()
            deq.append(i)
        
        # if new lesser, retain at back
        else:
            deq.append(i)

        i+=1

    return deq


class Solution(object):
    def maxSlidingWindow(self, nums, k):
        
        ans = []

        if not nums:
            return ans
        
        deq = deque()
        deq.append(0)
        deq = getHighestFirstK(deq, nums, k)
        
        # print([nums[i] for i in deq])
        ans.append(nums[deq[0]])

        i = k

        while i<len(nums):

            # remove irrelevant from deq (out of window)
            while deq and deq[0] <= i-k:
                deq.popleft()
            

            # remove  all indices of numbers lesser than current
            while deq and nums[deq[-1]] < nums[i]:
                deq.pop()
            
            # insert element from right
            deq.append(i)
            
            # print(nums[deq[0]])
            ans.append(nums[deq[0]])
            i+=1
        
        return ans






# nums = [1,3,-1,-3,5,3,6,7]
# k = 3

# nums = [1,3,-1,-3,5,3,6,7]
# k = 1

# nums = [1,3,-1,-3,5,3,6,7]
# k = 0


nums = [9,10,9,-7,-4,-8,2,-6]
k = 5

print(nums)
sol = Solution().maxSlidingWindow(nums, k)
print(sol)