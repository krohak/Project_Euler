from string import ascii_lowercase

mapping = {}
for i, letter in enumerate(ascii_lowercase):
    mapping[i+1] = letter


class Solution:
    def numDecodings(self, s): 
        
        global mapping

        L = [0 for char in s]
        L.append(0)
        L[0] = 1

        n = len(L)

        i = 0
        while i<n:
            
            if i-1 >= 0:
                if not s[i-1] == '0':
                    L[i] += L[i-1]

            if i-2>=0:
                if int(s[i-2]+s[i-1]) in mapping and not s[i-2] == '0':
                    L[i] += L[i-2]

            i+=1

        return L[n-1]


num = "2226"
num = "1011"
num = "100"
num = "110"
num = "1001"
num = "12120"
num = "10"
sol = Solution().numDecodings(num)
print(sol)