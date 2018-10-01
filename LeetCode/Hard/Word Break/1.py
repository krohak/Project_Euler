class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        
        wordDict = set(wordDict)

        L = [set([0]) for char in s]
        # L[0].add(0)
        L.append(set([0]))
        
        n = len(s)

        i = 0
        # start = 0
        while i<n+1:
            
            # L[i] = 
            L_this = set()
            this_bool = 0
            
            for start in L[i-1]:

                if s[start:i] in wordDict:
                    L_this.add(i)
                    this_bool=1
            
            # if this_bool:
            L[i] = L_this.union(L[i-1])

            # else:
            #     L[i] = L[i-1]

            i+=1

        # print(L)
        return this_bool==True


# s = "leetcode"
# wordDict = ["leet","co","de"]

s = "catsandog"
wordDict = ["cats", "dog", "sand", "and", "cat",]

# s = "applepenapple"
# wordDict = ["apple", "pen"]


s = "aaaaaaa"
wordDict = ["aaaa","aaa"]

sol = Solution().wordBreak(s,wordDict)
print(sol)