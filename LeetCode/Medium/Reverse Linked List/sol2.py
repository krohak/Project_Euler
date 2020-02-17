# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    
    def __init__(self):
        self.new_head = None
    
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        self.rec(head)
        return self.new_head
        
    
    def rec(self, head):
        
        if not head:
            return None
        
        nxt = self.rec(head.next)
        if nxt:
            nxt.next = head
            head.next = None
        else:
            self.new_head = head
        
        return head