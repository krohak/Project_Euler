from collections import Counter, deque 


class Solution(object):
    def minWindow(self, s, t):

        if not s or not t:
            return ""

        deq = deque(s)

        s_set = Counter(s)
        t_set = Counter(t)

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

            
        print(deq)

s = "ADOBECODEBANC"
t = "ABC"
sol = Solution().minWindow(s,t)

