"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""
class Solution:
    def flatten(self, head):
        self.recursive_find_last_node_in_child(head)            
        return head
    
    def recursive_find_last_node_in_child(self, head):
        
        last_node = None
        while(head):
            if head.child:
                child_list_last = self.recursive_find_last_node_in_child(head.child)
                
                temp = head.next
                head.next = head.child
                head.child.prev = head
                head.child = None
                
                child_list_last.next = temp
                if temp:
                    temp.prev = child_list_last
                
            last_node = head    
            head = head.next   
            
        return last_node
            