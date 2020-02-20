# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        if m==n:
            return head
        
        counter = 1
        
        m_minus_one = None
        m_pointer = None
        n_minus_one = None
        n_pointer = None
        
        pointer = head
        
        while counter<m:
            m_minus_one = pointer
            pointer = pointer.next
            counter+=1
        
        m_pointer = pointer
        
        prev = None
        while counter<n+1:
            nxt = pointer.next
            pointer.next = prev
            prev = pointer
            pointer = nxt
            counter+=1
        
        n_minus_one = prev
        n_pointer = pointer
        
        if not m_minus_one:
            head = n_minus_one
        else:
            m_minus_one.next = n_minus_one
        if m_pointer:
            m_pointer.next = n_pointer
        
        return head