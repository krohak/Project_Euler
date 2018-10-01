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
        if s[0] == "0":
            return 0
        
        if len(s) == 1:
            return 1

        if int(s[0]+s[1]) in mapping and s[1]=="0" and len(s) == 2:
            return 1

        # print("hello",s)
        s = s+"x" # let s be s+"x"

        L = [0 for char in s]
        # print(L)

        n = len(s)
        i = 0
        while i < n-2:
            
            # print(s[i],s[i+1])
            if int(s[i]+s[i+1]) == 0:
                return 0

            if int(s[i]+s[i+1]) not in mapping: 
                
                # print("here",s[i]+s[i+1])
                if s[i+1]=="0":
                    return 0

                # else:
                #     pass

            elif not s[i] == "0":
                # if not s[i+2] == "0":
                L[i+2]+=1
            
            else:
                i+=1
                continue


            L[i+1]+=1
            i+=1
            

        print(L)
        return L[n-2]+L[n-1]


# num = "2226"
# num = "1011"
num = "100"
num = "110"
# num = "1001"
# num = "12120"
# num = "10"
# print(num)
sol = Solution().numDecodings(num)
print(sol)