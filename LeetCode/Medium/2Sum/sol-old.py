from collections import Counter

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        counterMap = Counter(nums)
        answer, other = [], None
        
        for i, num in enumerate(nums):
            counterMap[num]-=1
            if counterMap.get(target-num, 0):
                answer.append(i)
                other = target-num
                i+=1
                break
            counterMap[num]+=1
        
        while i<len(nums):
            if nums[i] == other: answer.append(i); break
            i+=1
            
        return answer