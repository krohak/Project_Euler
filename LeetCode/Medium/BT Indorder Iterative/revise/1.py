# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:

        stack = []

        curr = root

        ans = []
        

        while(curr or stack):

            while(curr):
                stack.append(curr)
                curr = curr.left
            
            
            curr = stack.pop()
            ans.append(curr.val)

            curr = curr.right

        return ans