# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:


        stack = []
        ans = []
        curr = root

        while(stack or curr):

            if(not curr):
                curr = stack.pop()
                ans.append(curr.val)
                curr = curr.right

            elif(curr.left):
                stack.append(curr)
                curr = curr.left
                
            
            elif(not curr.left):
                ans.append(curr.val)
                curr = curr.right

        return(ans)