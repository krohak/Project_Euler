class Solution:
    def canAttendMeetings(self, intervals):
        intervalsSorted = sorted(intervals)
        for i, (start, _) in enumerate(intervalsSorted):
            if i > 0 and start < intervalsSorted[i-1][1]: return False        
        return True