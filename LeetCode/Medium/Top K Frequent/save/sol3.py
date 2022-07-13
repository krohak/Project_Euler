from collections import Counter
import heapq

class Solution:
    def topKFrequent(self, nums, k):
        numsCount = list([(-v, k) for k, v in Counter(nums).items()])
        heapq.heapify(numsCount)
        return [heapq.heappop(numsCount)[1] for _ in range(k)]