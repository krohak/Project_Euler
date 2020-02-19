# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from collections import deque

class Solution:
    def isCousins(self, root, x, y) -> bool:
        
        frontier = deque()
        explored = set()
        depths = {}
        parents = {}
        depths[root.val] = 0 
        parents[root.val] = None
        
        frontier.append(root)
        
        while frontier:
            
            if x in depths and y in depths:
                break
            
            node = frontier.popleft()
            explored.add(node)
            
            for neighbour in self.neighbours(node):
                if neighbour not in frontier and neighbour not in explored:
                    
                    depths[neighbour.val] = depths[node.val]+1
                    parents[neighbour.val] = node.val
                    frontier.append(neighbour)
        
        return depths[x] == depths[y] and not parents[x] == parents[y]
    
    
    def neighbours(self, node):
        ngbs = []
        if node.left:
            ngbs.append(node.left)
        if node.right:
            ngbs.append(node.right)
        return ngbs
