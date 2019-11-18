""""
NOT WORKING
IN PROGRESS
"""
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    def __str__(self):
        return "{} {} {}".format(self.val, self.left, self.right)




def buildTree(preorder, inorder):

    if not preorder:
        return None

    elif len(preorder) == 1:
        return TreeNode(preorder[0])

    root = preorder[0]

    divider = inorder.index(root)

    left_inorder = inorder[:divider]
    if len(inorder) > divider+1:
        right_inorder = inorder[divider+1:]
    else:
        right_inorder = []


    if left_inorder:
        left_inorder_last = left_inorder[-1]
        left_preorder_end = preorder.index(left_inorder_last)
        left_preorder = preorder[1:left_preorder_end+1]
    else:
        left_preorder_end = 0
        left_preorder = []


    if len(preorder) > left_preorder_end+1:
        right_preorder = preorder[left_preorder_end+1:]
    else:
        right_preorder = []

    node = TreeNode(root)
    node.left = buildTree(left_preorder, left_inorder) if left_preorder else None
    node.right = buildTree(right_preorder, right_inorder) if right_inorder else None

    return node

preorder = [3, 9, 10, 18, 20, 15, 7]
inorder = [10, 9, 18, 3, 15, 20, 7]

preorder = [1,2,3]
inorder = [3,2,1]

node = buildTree(preorder, inorder)
print(node)