class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:

    def __init__(self):
        self.pre_index = 0

    def buildTreeRecCaller(self, preorder, inorder):
        in_start = 0
        in_end = len(inorder)-1

        tree = self.buildTreeRec(preorder, inorder, in_start, in_end)

        return tree

    def buildTreeRec(self, preorder, inorder, in_start, in_end):

        if self.pre_index >= len(preorder):
            return None

        num = preorder[self.pre_index]
        index = self.find_index(num, inorder)
        self.pre_index+=1

        node = TreeNode(num)

        node.left = self.buildTreeRec(preorder, inorder, 
                        in_start, index-1) if in_start <= index-1 else None
        node.right = self.buildTreeRec(preorder, inorder, 
                        index+1, in_end) if index+1 <= in_end else None

        return node

    def find_index(self, num, inorder):
        return inorder.index(num)
