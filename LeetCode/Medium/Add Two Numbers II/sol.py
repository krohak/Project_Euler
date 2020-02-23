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
        
        # diff = self.calculate_diff(l1,l2)
        # if diff>0:
        # elif diff<0:
        
        
        head, carry = self.rec_to_bottom(l1, l2)
        if carry:
            curr_node = ListNode(carry)
            curr_node.next = head
            return curr_node
        return head
    
    
    
    
    def add_carry_to_remaining(self, linked_list, carry, ans):
        pass
        
    def calculate_diff(self, l1, l2):
        len_l1 = 0
        len_l2 = 0
        p1 = l1
        p2 = l2
        
        while(p1 or p2):
            
            if p1:
                len_l1+=1
                p1 = p1.next
                
            if p2:
                len_l2+=1
                p2 = p2.next
        
        return len_l1-len_l2
        
    def rec_to_bottom(self, pointer_l1, pointer_l2):
        
        if not pointer_l1 and not pointer_l2:
            return None, 0
        
        elif not pointer_l1:
            child, carry = self.rec_to_bottom(pointer_l1, pointer_l2.next)
        
        elif not pointer_l2:
            child, carry = self.rec_to_bottom(pointer_l1.next, pointer_l2)
            
        else:
            child, carry = self.rec_to_bottom(pointer_l1.next, pointer_l2.next)
        
        x = 0 if not pointer_l1 else pointer_l1.val
        y = 0 if not pointer_l2 else pointer_l2.val
        
        total = x+y+carry
        
        curr_val = total%10
        carry = total//10
        
        curr_node = ListNode(curr_val)
        curr_node.next = child
        
        return curr_node, carry
        
        