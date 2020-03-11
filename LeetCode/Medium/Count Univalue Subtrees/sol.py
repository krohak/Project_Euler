# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    
    def __init__(self):
        
        self.uni_values = 0
        self.memo = {}
        
    def countUnivalSubtrees(self, root: TreeNode) -> int:
        
        if not root:
            return 0
        
        if self.is_uni_value(root):
            self.uni_values += 1
        
        self.countUnivalSubtrees(root.left)
        self.countUnivalSubtrees(root.right)
        
        return self.uni_values
    
    
    def is_uni_value(self, node):
        
        if node in self.memo:
            return self.memo[node]
        
        if not node.left and not node.right:
            return True
        
        left_uni_value = True
        if node.left: 
            left_uni_value = self.is_uni_value(node.left)
            
            if not node.left.val == node.val:
                self.memo[node] = False
                return self.memo[node]
        
        right_uni_value = True
        if node.right:
            right_uni_value = self.is_uni_value(node.right)
                
            if not node.right.val == node.val:
                self.memo[node] = False
                return self.memo[node]
            
        self.memo[node] = (left_uni_value and right_uni_value)
        return self.memo[node]
        