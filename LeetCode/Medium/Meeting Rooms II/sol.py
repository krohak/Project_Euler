import heapq

class Solution(object):
    def minMeetingRooms(self, intervals):
        sortedIntervals = sorted(intervals)
        rooms = [sortedIntervals[0][1]]
        heapq.heapify(rooms)
        for start, end in sortedIntervals[1:]:
            if start < rooms[0]:
                heapq.heappush(rooms, end)
            else:
                heapq.heapreplace(rooms, end)
        return len(rooms)