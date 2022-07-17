class Solution:
    def wiggleMaxLength(self, nums):
        n = len(nums)
        if n==0: return 0
        posSequence = [ 1 for _ in range(n) ]
        negSequence = [ 1 for _ in range(n) ]
        for x in range(n):
            for i in range(x):
                if nums[x] > nums[i]:
                    posSequence[x] = max(negSequence[i]+1, posSequence[x])
                elif nums[x] < nums[i]:
                    negSequence[x] = max(posSequence[i]+1, negSequence[x])
        return max(max(posSequence), max(negSequence))