# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:

        index = 1
        explored = set()

        parent = {}

        smallest = root
        next_smallest = smallest

        while(index<=k):
            
            while(smallest.left and smallest.left.val not in explored):
                
                next_smallest = smallest
                smallest = smallest.left

                parent[smallest.val] = next_smallest

            index+=1

            if(index == k+1):
                break

            smallest = next_smallest
            next_smallest = next_smallest.right

            parent[next_smallest.val] = smallest
            
            index+=1

            if(index == k+1):
                break
            
            next_smallest = parent[smallest]
            smallest = next_smallest

            index+=1

            if(index == k+1):
                break
            
            smallest = next_smallest
            next_smallest = next_smallest.right
