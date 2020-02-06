from collections import Counter

class Solution:
    def firstUniqChar(self, string) -> int:
        
        
        freq = Counter(string)
        
        for i in range(len(string)):
            if freq[string[i]] == 1:
                return i
            
        return -1