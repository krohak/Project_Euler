# Definition for a Node.
class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children if children is not None else []


class Solution(object):
    def __init__(self):
        self.explored = set()
        self.post = {}
        self.clock = 0

    def findRoot(self, tree):
        for node in tree:
            if node not in self.explored:
                self.dfs(node)
        time2node = { t:n for n,t in self.post.items() }
        return time2node [max(time2node.keys())]

    def dfs(self, node):
        self.explored.add(node)
        for child in node.children:
            if child not in self.explored:
                self.dfs(child)
        self.post[node] = self.clock
        self.clock+=1