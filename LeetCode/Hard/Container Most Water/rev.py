    
class Solution(object):
   
    def maxArea(self,arr):
        area = 0

        n = len(arr)

        left = 0
        right = n-1

        area = areaOf(left, right, arr)

        while left<right:

            area = max(area, areaOf(left, right, arr))

            if arr[left]<arr[right]:
                left+=1
            else:
                right-=1

        return area



def areaOf(i_h1, i_h2, arr):

    width = abs(i_h2-i_h1)

    return (arr[i_h1]*width if arr[i_h1] < arr[i_h2] else arr[i_h2]*width)




arr = [1,8,6,2,5,4,8,3,7]
area = Solution().maxArea(arr)      
print(area)