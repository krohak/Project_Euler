from collections import Counter, deque 
from copy import deepcopy

class Solution(object):
    def minWindow(self, s, t):

        if not s or not t:
            return ""
        
        if len(t) > len(s):
            return ""

        deq = deque(s)
        deq2 = deepcopy(deq)

        s_set = Counter(s)
        t_set = Counter(t)
        s_set2 = deepcopy(s_set)
        t_set2 = deepcopy(t_set)

        d1 = removeChars(1, deq, s_set, t_set)
        d2 = removeChars(0, deq2, s_set2, t_set2)

        # print(d1, d2)

        if len(d1) < len(d2):
            return ''.join(list(d1))
        else:
            return ''.join(list(d2))


def removeChars(right, deq, s_set, t_set):

        if right:
            popEnd(deq, s_set, t_set)
            popFront(deq, s_set, t_set)

        else:
            popFront(deq, s_set, t_set)
            popEnd(deq, s_set, t_set)

        return deq


def popEnd(deq, s_set, t_set):

    # pop from deq end
    while deq:
        
        # if char in t
        if(t_set[deq[-1]]):
            # check if we can remove from deq
            if s_set[deq[-1]] - 1 >= t_set[deq[-1]]:
                s_set[deq[-1]]-=1
                deq.pop()
            
            else:
                break

        # if char not in t
        else:
            deq.pop()

    return deq

def popFront(deq, s_set, t_set):

    # pop from front
    while deq:
    
        # if char in t
        if(t_set[deq[0]]):
            # check if we can remove from deq
            if s_set[deq[0]] - 1 >= t_set[deq[0]]:
                s_set[deq[0]]-=1
                deq.popleft()
            
            else:
                break

        # if char not in t
        else:
            deq.popleft()

    return deq

s = "ADOBECODEBANC"
t = "ABC"
ans = ""
sol = Solution().minWindow(s,t)
print(sol)
