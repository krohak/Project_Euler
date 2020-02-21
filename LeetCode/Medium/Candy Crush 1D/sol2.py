class Solution:

    def candy_crush(self, text):
        
        stack = []
        # 0 - (val, freq)

        i = 0
        while i<len(text):
            char = text[i]
            if stack:
                if char == stack[-1][0]:
                    val, freq = stack[-1]
                    freq+=1
                    stack[-1] = (val, freq)
                    i+=1
                    continue
                else:
                    _, freq = stack[-1]
                    if freq>=3:
                        stack.pop()
                        continue
            stack.append((char, 1))
            i+=1

        if stack and stack[-1][1] >=3:
            stack.pop()
        
        ans = ""
        for val, freq in stack:
            ans+=''.join([val]*freq)

        return ans


text = "aaabbbc"
# Output: "c"
text = "aabbbacd"
# Output: "cd"
text = "aabbccddeeedcba"
# Output: ""
text = "aaabbbacd"
# Output: "acd"


sol = Solution().candy_crush(text)
print(sol)