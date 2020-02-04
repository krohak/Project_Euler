class Solution:
    def lengthOfLongestSubstring(self, s):

        length = len(s)
        if not length:
            return 0

        pos_dict = {}
        max_substring = 0

        start, end = 0, 0
        while(start < length and end < length):
            
            if not s[end] in pos_dict:
                pos_dict[s[end]] = end
                
            else:
                for i in range(start, pos_dict[s[end]]):
                    pos_dict.pop(s[i], None)
                start=pos_dict[s[end]]+1
                pos_dict[s[end]] = end

            max_substring = max(max_substring, end-start+1)
            end+=1

        return max_substring

s = "llwpwke"
# s = "wpwke"
# s = "wpwpk"
# s = "abcabcbb"
sol = Solution().lengthOfLongestSubstring(s)
print(sol)