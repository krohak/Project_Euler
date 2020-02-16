# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        
        len_linked_list = 0
        pointer = head
        while(pointer):
            len_linked_list+=1
            pointer = pointer.next
            
        if not len_linked_list:
            return True
        
        first_half_index = len_linked_list//2 + 1
        
        pointer = head
        first_half_numbers = []
        for _ in range(1, first_half_index):
            first_half_numbers.append(pointer.val)
            pointer = pointer.next
        
        second_half_index = first_half_index
        if len_linked_list%2:
            second_half_index = first_half_index+1
            pointer = pointer.next
        
        second_half_numbers = []
        for _ in range(second_half_index, len_linked_list+1):
            second_half_numbers.append(pointer.val)
            pointer = pointer.next
        
        for x, y in zip(reversed(first_half_numbers), second_half_numbers):
            if not x==y:
                return False
        
        return True