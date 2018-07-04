# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# Algorithm: buildTreeIn()
# 1) Pick an element from Preorder. Increment a Preorder Index Variable (preIndex in below code) to pick next element in next recursive call.
# 2) Create a new tree node tNode with the data as picked element.
# 3) Find the picked element’s index in Inorder. Let the index be inIndex.
# 4) Call buildTree for elements before inIndex and make the built tree as left subtree of tNode.
# 5) Call buildTree for elements after inIndex and make the built tree as right subtree of tNode.
# 6) return tNode.

class Solution(object):
    
        
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        buildTreeIn.preIndex = 0
        return buildTreeIn(inorder, preorder, 0, len(inorder)-1)


def search(arr, start, end, value):
    for i in range(start, end+1):
        if arr[i] == value:
            return i

def buildTreeIn(inOrder, preOrder, inStrt, inEnd):

    if (inStrt > inEnd):
        return None

    # Pich current node from Preorder traversal using
    # preIndex and increment preIndex
    tNode = TreeNode(preOrder[buildTreeIn.preIndex])
    buildTreeIn.preIndex += 1

    # If this node has no children then return
    if inStrt == inEnd :
        return tNode

    # Else find the index of this node in Inorder traversal
    inIndex = search(inOrder, inStrt, inEnd, tNode.val)

    # Using index in Inorder Traversal, construct left 
    # and right subtrees
    tNode.left = buildTreeIn(inOrder, preOrder, inStrt, inIndex-1)
    tNode.right = buildTreeIn(inOrder, preOrder, inIndex+1, inEnd)

    return tNode
