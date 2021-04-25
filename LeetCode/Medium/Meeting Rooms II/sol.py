import heapq

class Solution:
    def minMeetingRooms(self, intervals: list) -> int:
        
        sortedIntervals = sorted(intervals)
        heap = [0]
        heapq.heapify(heap)
        rooms = 1
        
        for start, end in sortedIntervals:
            if start < heap[0]:
                rooms+=1
            else:
                heapq.heappop(heap)
            heapq.heappush(heap, end)
            
        return rooms