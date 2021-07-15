class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        self.flattenLeft(root)
    
    def flattenLeft(self, root: TreeNode) -> None:
        if not root: 
            return 
        
        self.flattenLeft(root.left)
        self.flattenLeft(root.right)
        
        rightSave = root.right
        root.right = root.left
        root.left = None
        
        rightMost = root
        while(rightMost.right):
            rightMost = rightMost.right
            
        rightMost.right = rightSave