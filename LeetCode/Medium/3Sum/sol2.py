class Solution(object):

    def threeSum(self, arr):
        
        arr.sort()
        
        length = len(arr)
        
        answer = []
        
        i = 0
        while i<length:
            
            if (i > 0 and arr[i] == arr[i - 1]):
                i+=1
                continue
            
            left = i + 1
            right = length-1
            
            while (left<right):
                                
                sum_current = arr[i] + arr[left] + arr[right]
                
                if sum_current>0:
                    right-=1
                
                elif sum_current<0:
                    left+=1
                
                else:
                    
                    answer.append([arr[i], arr[left], arr[right]])

                    while(left < right and arr[left] == arr[left+1]):
                        left+=1

                    while(left < right and arr[right] == arr[right-1]):
                        right-=1
                    
                    left+=1
                    right-=1
            i+=1
        
        return answer