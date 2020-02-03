# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from collections import deque

class Solution:
    
    # def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
    def lowestCommonAncestor(self, root, p, q):
        
        # travel down from root and find p
        # and q to build its parent pointer dict

        parent_dict = self.bfs(root, p, q)

        # make set of all parents of p
        # by going up the parent pointer dict

        p_parent_set = self.go_up_parents(p, parent_dict)

        # go up q's parent pointer dict,
        # keep checking in p parent set
        # return first match

        common_parent = self.check_parents(q, p_parent_set, parent_dict)
        return common_parent

    def check_parents(self, node, other_parent_set, parent_dict):

        while node:
            if node.val in other_parent_set:
                return node
            node = parent_dict[node.val]

    def go_up_parents(self, node, parent_dict):
        all_parents = set()

        while node:
            all_parents.add(node.val)
            node = parent_dict[node.val]

        return all_parents    

    def bfs(self, root, p, q):

        p_found = False
        q_found = False

        frontier = deque()
        explored = set()
        parent_dict = {}

        frontier.append(root)
        parent_dict[root.val] = None 

        while(frontier and (not p_found or not q_found)):
            node = frontier.popleft()
            explored.add(node)

            for neighbour in self.neighbours(node):
                if neighbour not in explored and neighbour not in frontier:
                    parent_dict[neighbour.val] = node
                    frontier.append(neighbour)
                    if neighbour.val == p.val:
                        p_found = True
                    elif neighbour.val == q.val:
                        q_found = True

        return parent_dict

    def neighbours(self, node):

        if node.left:
            yield node.left
        if node.right:
            yield node.right
            