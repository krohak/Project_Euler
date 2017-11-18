"""
Detect a cycle in a linked list. Note that the head pointer may be 'None' if the list is empty.


A Node is defined as: 
""" 
class Node(object):
    def __init__(self, data = None, next_node = None):
        self.data = data
        self.next = next_node


def has_cycle(head):
    node1=head
    node2=head.next
    
    while(node1 != node2 and node1 != None and node2 != None):
        node1 = head.next
        node2 = head.next.next.next
        
    if(node1 == None or node2 == None):
        return 0
    
    elif(node1 == node2):
        return 1
            
    

