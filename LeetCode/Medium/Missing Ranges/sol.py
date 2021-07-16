class Solution:
    def findMissingRanges(self, nums, lower, upper):
        if not nums:
            return [self.getRangeString(lower, upper)]
        
        missingRanges = []
        if not lower == nums[0]: 
            missingRanges.append(self.getRangeString(lower, nums[0]-1))
        for i in range(1, len(nums)):
            if not nums[i-1] == nums[i]-1:
                missingRanges.append(self.getRangeString(nums[i-1]+1, nums[i]-1))
        if not upper == nums[-1]: 
            missingRanges.append(self.getRangeString(nums[-1]+1, upper))
        return missingRanges
    
    def getRangeString(self, lower, upper):
        if lower == upper:
            return str(lower)
        return "{}->{}".format(lower, upper)
        