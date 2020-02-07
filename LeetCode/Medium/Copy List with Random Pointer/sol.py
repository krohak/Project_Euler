# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

class Solution:
    def copyRandomList(self, head):
        
        if not head:
            return
        
        node_dict = {}
        
        head_copy = head
        while(head_copy):    
            node_dict[head_copy] = Node(head_copy.val)
            head_copy = head_copy.next
        
        head_copy = head
        while(head_copy):
            node = node_dict[head_copy]
            if head_copy.next:
                node.next = node_dict[head_copy.next]
            if head_copy.random:
                node.random = node_dict[head_copy.random]
            head_copy = head_copy.next
        
        return node_dict[head]