class Solution:
    def trap(self, height):
        
        if not height:
            return 0


        left = 0
        right = len(height)-1


        max_left = 0
        max_right = 0

        water_trapped = 0

        while (left<=right):

            if (height[left] < height[right]):

                max_left = max(height[left], max_left)
                water_trapped+= max_left - height[left]
                left+=1

            else:  

                max_right = max(height[right], max_right)
                water_trapped+= max_right - height[right]
                right-=1

        return water_trapped