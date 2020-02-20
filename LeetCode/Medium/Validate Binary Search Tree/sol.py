# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        return self.is_valid_rec(root, -float('inf'), float('inf'))
    
    
    def is_valid_rec(self, root, lower_bound, upper_bound):
        
        if not root:
            return True
        
        if not lower_bound <= root.val or not root.val <= upper_bound:
            return False
        
        return self.is_valid_rec(root.left, lower_bound, root.val-1) and self.is_valid_rec(root.right, root.val+1, upper_bound)