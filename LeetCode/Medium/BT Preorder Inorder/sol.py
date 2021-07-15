# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def __init__(self):
            self.preIndex = 0
            
    def buildTree(self, preorder, inorder) -> TreeNode:
        
        if not inorder:
            return None
        
        node = TreeNode()
        node.val = preorder[self.preIndex]; self.preIndex+=1
        inIndex = inorder.index(node.val)
        node.left, node.right = self.buildTree(preorder, inorder[:inIndex]), self.buildTree(preorder, inorder[inIndex+1:])
        return node