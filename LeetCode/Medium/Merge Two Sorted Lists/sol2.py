# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        mergedList = ListNode()
        mergedListPointer = mergedList
            
        while l1 and l2:
            mergedListPointer.next = ListNode( val= min(l1.val, l2.val) )
            if l1.val<l2.val: l1=l1.next
            else: l2=l2.next
            mergedListPointer = mergedListPointer.next
        
        while l1:
            mergedListPointer.next = ListNode( val= l1.val )
            l1, mergedListPointer = l1.next, mergedListPointer.next
            
        while l2:
            mergedListPointer.next = ListNode( val= l2.val )
            l2, mergedListPointer = l2.next, mergedListPointer.next
        
        return mergedList.next