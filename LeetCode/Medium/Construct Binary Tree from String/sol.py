class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def str2tree(self, s):
        stack = [TreeNode()]
        for c in s:
            if c!='(' and c!=')':
                node = TreeNode(int(c))
                parent = stack[-1]
                if not parent.left: parent.left = node
                else: parent.right = node
                stack.append(node)
            elif c==')':
                stack.pop()
        return stack.pop()