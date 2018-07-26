

def areaof (left, right, arr):
    h = min(arr[left],arr[right])
    b = right-left
    area = h*b
    return area
    
    
    
class Solution(object):
   
    def maxArea(self,arr):
        if len(arr)<=1:
            return 0
            
        if len(arr)%2==0:
            arr.append(0)
        
        n_half = len(arr) // 2
        mid = n_half
        
        left = mid
        right = mid
        
        
        area = areaof(left, right, arr)
        
        
        for i in range(n_half):
            left_dash = mid - (i+1)
            right_dash = mid + (i+1)
            
            
    
            a1 = areaof(left_dash, right, arr)
            # left and right-dash
            a2 = areaof (left, right_dash, arr)
            # left: dash and right-dash
            a3 = areaof(left_dash, right_dash,arr)
            max_area = max(area, a1, a2, a3)
            
            if max_area == a1:
                left = left_dash
                area = a1
            
            elif max_area == a2:
                right = right_dash
                area = a2
                
            elif max_area == a3:
                left = left_dash
                right = right_dash
                area = a3
    
        return area
        

arr = [3,3]
arr = [1,8,6,2,5,4,8,3,7]
solobj = Solution()
area = solobj.maxArea(arr)      
print(area)
    
