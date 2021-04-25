from collections import Counter

class Solution:
    def twoSum(self, nums: list, target: int) -> list:
        indexDict = {}
        for i, num in enumerate(nums):
            if target-num in indexDict:
                return [i, indexDict[target-num]]
            indexDict[num] = i