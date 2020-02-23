# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if not l1:
            return l2
        if not l2:
            return l1
        
        
        ans = None
        ans_return = None
        prev = None
        
        carry_over = 0
        
        while(l1 and l2):
            
            sum_at_ones = (l1.val+l2.val+carry_over)%10 
            carry_over = (l1.val+l2.val+carry_over)//10
            
            ans = ListNode(sum_at_ones)
            if not prev:
                ans_return = ans
            else:
                prev.next = ans
            
            prev = ans
            l1 = l1.next
            l2 = l2.next
        
        while(l1):
            
            sum_at_ones = (l1.val+carry_over)%10 
            carry_over = (l1.val+carry_over)//10
            
            ans = ListNode(sum_at_ones)
            prev.next = ans
            
            prev = ans
            l1 = l1.next

        while(l2):
            
            sum_at_ones = (l2.val+carry_over)%10 
            carry_over = (l2.val+carry_over)//10
            
            ans = ListNode(sum_at_ones)
            prev.next = ans
            
            prev = ans
            l2 = l2.next
        
        if carry_over:
            ans = ListNode(carry_over)
            prev.next = ans
        
        return ans_return
                