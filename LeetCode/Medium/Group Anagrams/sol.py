from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs):
        
        counter_dict = defaultdict(list)
        
        for word in strs:
            
            char_list = [0]*26
            
            for char in word:
                char_list[ord(char)-ord('a')] += 1
            
            counter_dict[tuple(char_list)].append(word)
        
        ans = [ l for l in counter_dict.values()]
        return ans
        
            
        