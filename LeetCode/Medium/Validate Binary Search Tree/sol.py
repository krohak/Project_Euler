# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        return self.validBST(root, -float('inf'), float('inf'))
    
    def validBST(self, node, lowerBound, upperBound):
        if not node:
            return True
        
        if node.val >= lowerBound and node.val <= upperBound: 
            return self.validBST(node.left, lowerBound, node.val-1) and self.validBST(node.right, node.val+1, upperBound)
        return False