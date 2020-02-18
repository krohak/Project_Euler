# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

import heapq

class Solution:
    def mergeKLists(self, lists):
        
        k = len(lists)
        
        if not k:
            return None
        if k == 1:
            return lists[0]
        
        
        ans_linked_list = None
        head_of_ans = ans_linked_list
        
        list_pointers = [ lists[i] for i in range(k) ]
        
        
        pq = []
        
        for i in range(k):
            list_head = lists[i]
            if list_head:
                pq.append((list_head.val,i))
            
        
        heapq.heapify(pq)
        
        
        while(pq):
            
            min_element = heapq.heappop(pq)
            if not ans_linked_list:
                ans_linked_list = ListNode(min_element[0])
                head_of_ans = ans_linked_list
            else:
                ans_linked_list.next = ListNode(min_element[0])
                ans_linked_list = ans_linked_list.next
            
            index_list_pointer = min_element[1]
            l_pointer = list_pointers[index_list_pointer]
            l_pointer = l_pointer.next
            if l_pointer:
                heapq.heappush(pq, (l_pointer.val, index_list_pointer))
                list_pointers[index_list_pointer] = l_pointer
        
        return head_of_ans
