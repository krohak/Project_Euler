class Solution:
    def searchRange(self, nums, target):
        startLeft = endLeft = startMid = endMid = 0
        startRight = endRight = len(nums)-1
        
        while startLeft < startRight and endLeft < endRight:
            
            startMid = (startLeft+startRight)//2
            endMid = (endLeft+endRight)//2
            
            if startLeft < startRight:
                print(startLeft, startMid, startRight)
                if nums[startMid] < target:
                    startLeft = startMid + 1
                elif nums[startMid] > target:
                    startRight = startMid - 1
                elif nums[startMid]==nums[startMid-1]:
                    startRight = startMid - 1
                    
            if endLeft < endRight:
                if nums[endMid] < target:
                    endLeft = endMid + 1
                elif nums[endMid] > target:
                    endRight = endMid - 1
                elif nums[endMid]==nums[endMid+1]:
                    endLeft = endMid + 1
        
        return [startMid, endMid]