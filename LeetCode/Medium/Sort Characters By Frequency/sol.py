from collections import Counter

class Solution(object):
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        
        char_to_freq = Counter(s)
        
        freq_to_char = {}
        
        for char, freq in char_to_freq.items():
            
            if freq in freq_to_char:
                freq_to_char[freq].append(char)
            else:
                freq_to_char[freq] = [char]
                
                
        ans_string = ""
        len_s = len(s)
        for i in range(len_s, 0, -1):
            char_list = freq_to_char.get(i,[])
            for char in char_list:
                char_string = i*char
                ans_string = "{}{}".format(ans_string, char_string)
        
        return ans_string