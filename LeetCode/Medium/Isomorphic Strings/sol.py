class Solution(object):
    def isIsomorphic(self, s, t):
        s2t, t2s = {}, {}
        for s1, t1 in zip(s, t):
            if s1 in s2t and s2t[s1]!=t1:
                return False
            elif t1 in t2s and t2s[t1]!=s1:
                return False
            s2t[s1] = t1
            t2s[t1] = s1
        return True