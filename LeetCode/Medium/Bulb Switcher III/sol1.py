class Solution:
    def numTimesAllBlue(self, light):
        
        boolean_array = [0 for _ in light]
        
        on_bulbs = 0
        consecutive_on = 0
        blue_moments = 0
        
        for bulb in light:
            
            on_bulbs+=1
            
            boolean_array[bulb-1] = 1
            
            while consecutive_on < len(light) and boolean_array[consecutive_on]:
                consecutive_on+=1
            
            if (consecutive_on == on_bulbs):
                blue_moments+=1
        
        return blue_moments