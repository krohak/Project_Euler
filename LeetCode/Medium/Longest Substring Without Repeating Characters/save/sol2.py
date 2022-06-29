class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        doneLetters = {}
        
        maxLen = 0
        currLen = 0
        i = 0
        
        while i < len(s):
            
            if s[i] in doneLetters:
                maxLen = max(currLen, maxLen)
                currLen = 0
                i=doneLetters[s[i]]+1
                doneLetters = {}
            
            else:
                doneLetters[s[i]] = i
                currLen+=1
                i+=1
        
        return max(currLen, maxLen)