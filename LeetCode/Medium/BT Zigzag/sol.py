class Solution:
    def zigzagLevelOrder(self, root):

        if not root:
            return []

        ans = []
        direction = 1

        stack_right = []
        stack_left = []

        stack_right.append(root)
        while(stack_left or stack_right):
            
            ans_nest = []

            if direction:
                
                while(stack_right):
                    curr = stack_right.pop()
                    ans_nest.append(curr.val)
                    stack_left.append(curr.left) if curr.left else None
                    stack_left.append(curr.right) if curr.right else None
                

            else:
                
                while(stack_left):
                    curr = stack_left.pop()
                    ans_nest.append(curr.val)
                    stack_right.append(curr.right) if curr.right else None
                    stack_right.append(curr.left) if curr.left else None

            ans.append(ans_nest)
            direction = 1-direction             

        return ans