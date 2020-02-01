"""
Definition for a Node.
"""
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        self.zip(root)
        return root

    def zip(self, root):

        if root:
            left = root.left
            right = root.right
            
            while left and right:
                left.next = right
                left = left.right
                right = right.left

            self.zip(root.left)
            self.zip(root.right)