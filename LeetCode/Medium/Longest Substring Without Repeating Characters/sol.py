class Solution(object):
    def lengthOfLongestSubstring(self, s):
        if not s: return 0
        start, end = 0, 1
        encounteredDict = {s[start]:start}
        maxSubs = 0
        while end < len(s):
            if s[end] in encounteredDict:
                maxSubs = max(end-start, maxSubs)
                start = max(encounteredDict[s[end]]+1, start)
            encounteredDict[s[end]] = end
            end+=1
        return max(end-start, maxSubs)