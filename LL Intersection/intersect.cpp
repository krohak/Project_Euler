/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
class Solution {
public:
    ListNode *getIntersectionNode(ListNode *headA, ListNode *headB) {
        
        int len_a = 0;
        int len_b = 0;
        
        ListNode *headAref =  headA;
        ListNode *headBref = headB;
        
        
        while (headA != NULL){
            len_a++;
            headA = headA->next;
        }
        
        while (headB != NULL){
            len_b++;
            headB = headB->next;
        }
        
        int len_extra = 0;
        headA = headAref;
        headB = headBref;
        
        if (len_a > len_b){
            len_extra = len_a - len_b;
            
            for(int i=0; i<len_extra; i++){
                headA = headA -> next;
            }
        }
        
        else if (len_b > len_a){
            len_extra = len_b - len_a;
            
            for(int i=0; i<len_extra; i++){
                headB = headB -> next;
            }
        }
        
        while(headA != NULL && headB != NULL && headA->val !=headB->val){
            headA = headA -> next;
            headB = headB -> next;
        }
        
        
        return headA;
        
        
    }
};
