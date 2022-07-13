from collections import Counter
import heapq

class Solution(object):
    def topKFrequent(self, words, k):
        counts = Counter(words)
        countHeap = [ (-c,w) for w,c in counts.items() ]
        heapq.heapify(countHeap)
        return [ w for c, w in heapq.nsmallest(k, countHeap) ]
