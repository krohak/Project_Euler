from copy import deepcopy

class Solution(object):
    def lengthOfLIS(self, nums):
        if not nums:
            return 0
        
        reverse_dag = createDAG(nums)

        L = [0 for num in nums]
        n = len(nums)

        for j in range(n):
            max_len = 0
            for i, in_node in enumerate(reverse_dag[j]):
                if in_node == 1 and L[i] > max_len:
                    max_len = L[i]

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

    reverse_dag = deepcopy(dag)

    x = 0
    while x<n:
        y = 0
        while y<n:
            reverse_dag[x][y] = dag[y][x]
            y+=1
        x+=1

    return reverse_dag