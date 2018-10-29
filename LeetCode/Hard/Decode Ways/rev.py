from string import ascii_lowercase

mapping = {}
for i, char in enumerate(ascii_lowercase):
    mapping[i+1] = char


class Solution:
    def numDecodings(self, s):
        
        global mapping


        L = [0 for char in s]
        L.append(0)
        L[0] = 1

        i = 0
        n = len(L)
        while i < n:

            if i-1 >= 0:
                if s[i-1] != '0':
                    L[i]+=L[i-1]

            if i-2 >= 0:
                if s[i-2] != '0' and int(s[i-2]+s[i-1]) in mapping:
                    L[i]+=L[i-2]
            
            i+=1
        
        return L[n-1]


s= "226"
sol = Solution().numDecodings(s)
print(sol)