from copy import deepcopy
branches = []


class Solution(object):
    def wordBreak(self, s, wordDict):
        
        wordDict = set(wordDict)
        
        n = len(s)

        table = {}

        for i in range(n):
            table[i+1] = set()

        L = set([0])
        i = 1

        while i<n+1:
            
            L_this = set()

            for start in L:

                if s[start:i] in wordDict:
                    L_this.add(i)
                    table[i].add(start)
            

            L = L_this.union(L)

            i+=1

        # print(L)
        # print(table)

        tableDFSRecursiveCaller(table, n)

        global branches

        r_list = []
        for branch in branches:
            n = len(branch)

            r_string = ""
            i=1
            while i<n:
                if i==1:
                    r_string += s[branch[n-i]:branch[n-i-1]]
                else:
                    r_string = r_string + " " + s[branch[n-i]:branch[n-i-1]]
                i+=1
            r_list.append(r_string)

        # print(r_list)
        return r_list



def tableDFSRecursiveCaller(table, n):
    
    global branches
    branches = []
    branch = []
    node = n

    tableDFSRecursive(node, branch, table)
    


def tableDFSRecursive(node, branch, table):

    branch = deepcopy(branch)

    if not node == 0:
        branch.append(node)
        for neighbour in table[node]:
            tableDFSRecursive(neighbour, branch, table)

    else:
        global branches
        branch.append(node)
        branches.append(branch)
        return


s = "catsandog"
wordDict = ["cats", "dog", "sand", "and", "cat","og"]

s = "leetcode"
wordDict = ["leet","co","de"]


s = "pineapplepenapple"
wordDict = ["apple", "pen", "applepen", "pine", "pineapple"]

# print(s)
sol = Solution().wordBreak(s,wordDict)
print(sol)