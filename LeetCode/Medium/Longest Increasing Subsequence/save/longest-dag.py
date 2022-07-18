# from copy import deepcopy

class Solution(object):
    def lengthOfLIS(self, nums):
        if not nums:
            return 0
        
        dag = createDAG(nums)

        L = [0 for num in nums]
        n = len(nums)

        for j in range(n):
            max_len = 0
            i = 0
            while i < n:
                if dag[i][j] == 1 and L[i] > max_len:
                    max_len = L[i]
                i+=1

            L[j] = 1+max_len

        return max(L)


def createDAG(nums):

    n = len(nums)

    x = 0

    dag = []

    while x<n:
        y = 0
        candidates = []
        while y<n:
            if nums[y] > nums[x] and y > x:
                candidates.append(1)
            else:
                candidates.append(0)
            y+=1
        dag.append(candidates)
        x+=1

    return dag

nums = [1,2,3]
sol = Solution().lengthOfLIS(nums)
print(sol)