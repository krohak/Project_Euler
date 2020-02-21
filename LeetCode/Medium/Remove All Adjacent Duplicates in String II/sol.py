class Solution(object):
    def removeDuplicates(self, text, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        
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
                    val, freq = stack[-1]
                    if freq>=k:
                        if freq%k == 0:
                            stack.pop()
                            continue
                        else:
                            stack[-1] = (val, freq%k)
                            
            stack.append((char, 1))
            i+=1

        if stack:
            if stack[-1][1]%k ==0:
                stack.pop()
            else:
                val, freq = stack[-1]
                stack[-1] = (val, freq%k)
        
        ans = ""
        for val, freq in stack:
            ans+=''.join([val]*freq)

        return ans