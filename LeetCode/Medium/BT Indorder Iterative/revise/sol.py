class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

'''
Think about it in recursive terms and then
formulate an iterative solution using stack
to keep track of recursive calls.

At a point, you will need to keep a pointer
to skip lines of code in the recursive call. Use None
to skip re-traversal of left sub tree and pop the call stack.
'''
class Solution:
    def inorderTraversal(self, root: TreeNode):
        
        stack = []
        answer = []
        cursor = root

        while(stack or cursor):

            while(cursor):
                stack.append(cursor.val)
                cursor = cursor.left

            cursor = stack.pop()
            answer.append(cursor)
            
            cursor = cursor.right





