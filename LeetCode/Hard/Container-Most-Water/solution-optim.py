

def areaof (left, right, arr):
    h = min(arr[left],arr[right])
    b = right-left
    area = h*b
    return area
    
    
    
class Solution(object):
   
    def maxArea(self,arr):
        if len(arr)<=1:
            return 0
        
        left = 0
        right = len(arr)-1
        
        
        area = areaof(left, right, arr)
        
        
        while left < right:
            
            area_dash = areaof(left, right, arr)
            area = max(area, area_dash)
            
            if arr[left]<arr[right]:
                left=left+1
            else:
                right=right-1
    
        return area
