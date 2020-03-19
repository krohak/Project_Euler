class Solution:
    def numTimesAllBlue(self, light):
        
        running_max = 0
        
        blue_moments = 0
        
        for moment, bulb in enumerate(light):
            
            running_max = max(running_max, bulb)
            
            if moment+1 == running_max:
                blue_moments+=1
            
        return blue_moments