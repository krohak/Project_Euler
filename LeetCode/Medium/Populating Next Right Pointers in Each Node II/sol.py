class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return
        
        if not root.left and not root.right:
            return root
        
        if(root.left and root.right):
            root.left.next = root.right
        
        to_point_node = root.right
        if not root.right:
            to_point_node = root.left
        
        nxt = root.next
        while( to_point_node and nxt):

            if nxt.left:
                to_point_node.next = nxt.left
                break
            elif nxt.right:
                to_point_node.next = nxt.right
                break
            else:
                nxt = nxt.next
        
        self.connect(root.right)
        self.connect(root.left)
        
        return root