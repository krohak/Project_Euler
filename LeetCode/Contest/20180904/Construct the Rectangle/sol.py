from math import sqrt

class Solution(object):
    def constructRectangle(self, area):
        
        for x in reversed(range(1,int(sqrt(area)+1))):
            if area % x == 0:
                return [area//x, x]


solobj = Solution().constructRectangle(4)
print(solobj)