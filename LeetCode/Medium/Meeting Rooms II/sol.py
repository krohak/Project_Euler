import heapq

class Solution:
    def minMeetingRooms(self, intervals):
        sortedIntervals = sorted(intervals)
        minEndings = [sortedIntervals[0][1]]
        
        heapq.heapify(minEndings)
        minRooms = 1
        
        for (start, end) in sortedIntervals[1:]:
            if start < minEndings[0]:
                minRooms+=1
            else:
                heapq.heappop(minEndings)
            heapq.heappush(minEndings, end)
            
        return minRooms