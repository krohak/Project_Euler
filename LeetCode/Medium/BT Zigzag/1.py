class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        
        if not root:
            return []

        alternate = 0

        stack_left_to_right = []
        stack_right_to_left = []

        stack_left_to_right.append(root)

        answer = []

        while(stack_left_to_right or stack_right_to_left):

            if not alternate:
                ans = []
                while(stack_left_to_right):
                    root = stack_left_to_right.pop()
                    ans.append(root.val)
                    for neighbour in left_to_right_neighbours(root):
                        stack_right_to_left.append(neighbour)
                if ans: answer.append(ans)
                alternate = 1
            
            if alternate:
                ans = []
                while(stack_right_to_left):
                    root = stack_right_to_left.pop()
                    ans.append(root.val)
                    for neighbour in right_to_left_neighbours(root):
                        stack_left_to_right.append(neighbour)
                if ans: answer.append(ans) 
                alternate = 0

        return answer

def left_to_right_neighbours(root):
    if root.left:
        yield root.left
    if root.right:
        yield root.right


def right_to_left_neighbours(root):
    if root.right:
        yield root.right
    if root.left:
        yield root.left