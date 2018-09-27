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
        
        if len(s) == 1:
            return 1
        
        global mapping

        L = [0 for char in s]

        prev_char = s[0]

        i = 1
        for char in s[1:]:
            
            if char == "0" or prev_char == "0":
                # L[i] = L[i-1]
                print("here0", prev_char, char, i ,L[i])
            
            else:
                if not i-1 == 0:
                    L[i] = L[i-1]
                    print("here1", prev_char, char, i ,L[i])
                else:
                    L[i] = 1
            

            # treat prev_char+char as a seperate char
            if int(prev_char+char) in mapping and not prev_char == "0":
                
                if i-2 >= 0:
                    L[i] =  L[i] + L[i-2] + 1
                    print("here2", prev_char, char, i ,L[i])
                
                else:
                    L[i] = L[i] + 1
                    print("here3", prev_char, char, i ,L[i])

           
            prev_char = char
            i+=1

        print(L)
        return L[len(s)-1]

num = "2226"
num = "1011"
print(num)
sol = Solution().numDecodings(num)
print(sol)