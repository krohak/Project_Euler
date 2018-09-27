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
        L[0] = 1

        prev_char = s[0]

        for i, char in enumerate(s[1:]):
            
            # use i+1 for L

            # treat prev_char+char as a seperate char
            
            if int(prev_char+char) in mapping:
                # print( int( prev_char+char))
                
                if i+1-2 >= 0:
                    L[i+1] = L[i+1-2] + L[i+1-1]
                    # print('hello')
                
                else:
                    L[i+1] = L[i+1-1]+1
                    # print("hey",L[i+1])

            else:

                if char == "0":
                    L[i+1] = L[i+1-1]
                
                else:
                    L[i+1] = L[i+1-1]+1

            prev_char = char


        # print(mapping)
        return L[len(s)-1]


# sol = Solution().numDecodings("2226")
sol = Solution().numDecodings("10")
print(sol)