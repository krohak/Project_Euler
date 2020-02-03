# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:

    def __init__(self):
        self.max_sum = float('-inf')

    def maxPathSum(self, root):
        self.rec(root)
        return self.max_sum
    
    def rec(self, root):

        if not root:
            return 0
        left_gain = max(self.rec(root.left),0)
        right_gain = max(self.rec(root.right),0)
              
        new_gain = root.val + left_gain + right_gain
        self.max_sum = max(self.max_sum, new_gain)

        max_gain = root.val + max(left_gain, right_gain)
        return max_gain