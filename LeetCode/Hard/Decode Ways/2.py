from string import ascii_lowercase

mapping = {}

for i, letter in enumerate(ascii_lowercase):
    mapping[i+1] = letter


class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        if s == "0":
            return 0
        
        global mapping

        L = [0 for char in s]
        # L[0] = 1

        prev_char = s[0]

        i = 1
        for char in s[1:]:
            
            if char == "0" or prev_char == "0":
                if not i == 0:
                    L[i] = L[i-1]
            
            else:
                if not i == 0:
                    L[i] = L[i-1]+1
                else:
                    L[0] += 1
            

            # treat prev_char+char as a seperate char
            if int(prev_char+char) in mapping:
                # print( int( prev_char+char))
                
                if i-2 >= 0:
                    L[i] = L[i-2] + L[i-1]
                    # print('hello')
                
                elif i-1 >= 0:
                    L[i] = L[i-1]+1
                    # print("hey",L[i+1])

                else:
                    L[0] += 1

            prev_char = char
            i+=1

        # print(mapping)
        return L[len(s)-1]


sol = Solution().numDecodings("2226")
# sol = Solution().numDecodings("1011")
print(sol)