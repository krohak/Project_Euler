class Node(object):
    def __init__(self, val=0, left=None, right=None, random=None):
        self.val = val
        self.left = left
        self.right = right
        self.random = random

class NodeCopy(object):
    def __init__(self, val=0, left=None, right=None, random=None):
        self.val = val
        self.left = left
        self.right = right
        self.random = random

class Solution(object):
    def copyRandomBinaryTree(self, root):
        if not root: return None
        tree2copy = {None:None}
        frontier = [root]
        while frontier:
            node = frontier.pop(0)
            copy = NodeCopy(node.val)
            tree2copy[node] = copy
            if node.left: frontier.append(node.left)
            if node.right: frontier.append(node.right)
        frontier = [root]
        while frontier:
            node = frontier.pop(0)
            copy = tree2copy[node]
            copy.left, copy.right, copy.random = tree2copy[node.left], tree2copy[node.right], tree2copy[node.random]
            if node.left: frontier.append(node.left)
            if node.right: frontier.append(node.right)
        return tree2copy[root]