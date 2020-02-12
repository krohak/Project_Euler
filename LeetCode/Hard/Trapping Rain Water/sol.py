class Solution:
    def trap(self, heights):
        
        if not heights:
            return 0
        
        len_heights = len(heights)
        
        left_highest = [0 for _ in heights]
        left_highest[0] = heights[0]
        
        for i in range(1, len_heights):
            if heights[i] > left_highest[i-1]:
                left_highest[i] = heights[i]
            else:
                left_highest[i] = left_highest[i-1]
        
        right_highest = [ 0  for _ in heights]
        right_highest[len_heights-1] = heights[len_heights-1]
        
        for i in range(len_heights-2, -1, -1):
            if heights[i] > right_highest[i+1]:
                right_highest[i] = heights[i]
            else:
                right_highest[i] = right_highest[i+1]
        
        water_trapped = 0
        for i in range(len_heights):
            to_add = min(left_highest[i], right_highest[i]) - heights[i]
            water_trapped+=to_add
            
        
        return water_trapped