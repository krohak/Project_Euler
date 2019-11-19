class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:

        stack = []
        ans = []
        index = 1

        while((root or stack) and index<=k):

            while(root):
                stack.append(root)
                root = root.left
            
            root = stack.pop()
            ans.append(root.val)
            index+=1

            root = root.right
        
        return ans[-1]
