# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def flatten(self, root):
        self.rec(root)

    def rec(self, root):

        if not root:
            return

        if not root.left and not root.right:
            return 
        else:
            self.rec(root.left)
            self.rec(root.right)

        if root.left:
            if root.right:
                temp = root.right
                root.right = root.left
                root.left = None
                curr = root.right
                while(curr.right):
                    curr = curr.right
                curr.right=temp
            else:
                root.right=root.left
                root.left = None
            