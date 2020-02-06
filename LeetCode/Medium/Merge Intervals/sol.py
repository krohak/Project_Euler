class Solution:
    def merge(self, intervals):
        
        def custom_comparator(x):
            return x[0]
        
        intervals = sorted(intervals, key=custom_comparator)

        first_index = 0
        second_index = 1
        
        length_intervals = len(intervals)
        
        while (second_index<length_intervals):
            first_interval = intervals[first_index]
            second_interval = intervals[second_index]
            
            end_first_interval = first_interval[1]
            
            start_second_interval = second_interval[0]
            end_second_interval = second_interval[1]
            
            if start_second_interval<= end_first_interval:
                
                if end_second_interval<= end_first_interval:
                    pass
                
                else:
                    first_interval[1] = end_second_interval
                
                intervals[second_index] = None
                
                
            if (intervals[second_index]):
                first_index = second_index
                
            second_index+=1
            
        intervals = [ interval for interval in intervals if interval ]
        return intervals
