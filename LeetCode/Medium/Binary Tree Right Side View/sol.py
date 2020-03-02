# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    
    def __init__(self):
        self.curr_depth = 0
        self.answer = []
    
    def rightSideView(self, root: TreeNode):
        
        self.dfs(root, 0)
        return self.answer
        
    def dfs(self, node, depth):
        
        if not node:
            return
        
        if depth == self.curr_depth:
            self.answer.append(node.val)
            self.curr_depth+=1
        
        neighbours = [node.right, node.left]
        
        for neighbour in neighbours:
            self.dfs(neighbour, depth+1)