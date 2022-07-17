from itertools import pairwise

class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        if not nums: return 0
        diffs = [ a-b for a,b in pairwise(nums) ]
        maxWiggle, prevNeg = 1, None
        for d in diffs:
            if prevNeg==None and d!=0:
                maxWiggle+=1
                if d<0: prevNeg=True
                elif d>0: prevNeg=False
            elif prevNeg and d>0:
                maxWiggle+=1
                prevNeg = False
            elif not prevNeg and d<0:
                maxWiggle+=1
                prevNeg = True
        return maxWiggle