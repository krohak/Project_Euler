from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        
        start = 0
        end = 0
        
        min_window = float('inf')
        
        min_start = 0
        min_end = 0
        
        freq_map_t = Counter(t)
        uniq_t = len(freq_map_t)
        freq_map_window = { char: 0 for char in t }
        formed = 0
        
        n = len(s)
        
        while start < n:
            while end < n and not formed==uniq_t:
                if s[end] in freq_map_window:
                    freq_map_window[s[end]] += 1
                    if freq_map_window[s[end]] == freq_map_t[s[end]]:
                        formed+=1
                end+=1
    
            while formed==uniq_t:             
                if end-start+1 < min_window:
                    min_window = end-start+1
                    min_start = start
                    min_end = end
                if s[start] in freq_map_window:
                    freq_map_window[s[start]] -= 1
                    if freq_map_window[s[start]] < freq_map_t[s[start]]:
                        formed-=1
                start+=1

            if end==n and not formed==uniq_t:
                break
    
        return s[min_start:min_end] if not min_window == float('inf') else ""