class Solution:
    def merge(self, intervals):
        
        if len(intervals) < 2:
            return intervals
        
        sortedIntervals  = sorted(intervals) #nlogn
        merged = [sortedIntervals[0]]
        
        for i in range(1, len(sortedIntervals)):
            _, endx =  merged[-1]
            starty, endy = sortedIntervals[i]
            if starty <= endx:                
                if endy > endx:
                    merged[-1][-1] = endy
            else:
                merged.append([starty, endy])
        return merged