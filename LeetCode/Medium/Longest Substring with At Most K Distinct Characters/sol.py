from collections import defaultdict

class Solution:
    def removeFromSet(self, distinctSet, key):
        distinctSet[key]-=1
        if distinctSet[key] == 0:
            del distinctSet[key]
            
    def lengthOfLongestSubstringKDistinct(self, inputString: str, k: int) -> int:
        distinctSet = defaultdict(int)
        maxSubsLen = 0
        left, right = 0, 0
        while right < len(inputString):
            distinctSet[inputString[right]]+=1
            while len(distinctSet) > k:
                self.removeFromSet(distinctSet, inputString[left])
                left+=1 
            maxSubsLen = max(right-left+1, maxSubsLen)
            right+=1
        return maxSubsLen