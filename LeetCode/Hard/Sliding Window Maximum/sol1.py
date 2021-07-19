from collections import deque
idxi, numi = 0, 1

class Solution:
    def maxSlidingWindow(self, arr, k):
        
        slidingMax = []
        dq = deque([(0, arr[0])])
        for i in range(1, k):
            while dq and dq[-1][numi] < arr[i]:
                dq.pop()
            dq.append((i, arr[i]))
        slidingMax.append(dq[0][numi])

        for i in range(k, len(arr)):
            if dq and dq[0][idxi] < i-k+1:
                dq.popleft()
            while dq and dq[-1][numi] < arr[i]:
                dq.pop()
            dq.append((i, arr[i]))
            slidingMax.append(dq[0][numi])

        return slidingMax



# arr = [1,3,-1,-3,5,3,6,7]
# k = 3
# print(slidingWindowMaximum(arr, k))


# i = 0
# win = [(1, 3), (2, -1)] #pos, value
# output = 3

# i = 1
# win = [(1, 3), (2, -1), (3, -3)]
# output = 3

# i = 2
# win = [(4, 5)]
# output = 5

# i = 3
# win = [(4, 5), (5, 3)]
# output = 5

# i = 4
# win = [(6, 6)]
# output = 6

# i = 5
# win = [(7, 7)]
# output = 7

# [3,3,5,5,6,7]