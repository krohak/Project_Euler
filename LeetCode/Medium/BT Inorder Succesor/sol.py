# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:

    def inorderSuccessor(self, root: 'TreeNode', node: 'TreeNode') -> 'TreeNode':

        if node.right:
            return self.find_min_subtree(node.right)
        else:
            return self.find_min_parent(root, node)

    

    def find_min_subtree(self, node):
        while node.left:
            node = node.left

        return node


    def find_min_parent(self, root, node):

        succesor = None
        
        while root:
            if root.val < node.val:
                root = root.right
            elif root.val > node.val:
                succesor = root
                root = root.left
            else:
                return succesor