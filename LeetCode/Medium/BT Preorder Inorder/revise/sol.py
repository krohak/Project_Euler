class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    def __str__(self):
        return "{} {} {}".format(self.val, self.left, self.right)


class Solution:
    
    def __init__(self):
        self.preIndex = 0
        
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:

        instart, inend = 0, len(inorder)-1
        # self.buildTreeRec.preIndex = 0
        return self.buildTreeRec(preorder, inorder, instart, inend)

    def buildTreeRec(self, preorder, inorder, instart, inend):


        if instart>inend:
            return None

        node = TreeNode(preorder[self.preIndex])
        self.preIndex+=1

        if not preorder:
            return node

        index = search(inorder, instart, inend, node.val)

        node.left = self.buildTreeRec(preorder, inorder, instart, index-1)
        node.right = self.buildTreeRec(preorder, inorder, index+1, inend)

        return node


def search(inorder, instart, inend, nodeval):

    i = instart
    while i<=inend:
        if inorder[i] == nodeval:
            return i
        i+=1

