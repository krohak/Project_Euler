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

        print(L)
        print(table)

        tableDFSRecursiveCaller(table, n)

        return 1

def tableDFSIterative(table, n):

    frontier = []
    explored = set([0])

    frontier.append(n)

    while frontier:

        node = frontier.pop()

        if node not in explored:
            explored.add(node)
            print(node)

            for neighbour in table[node]:
                if neighbour not in explored:
                    
                    frontier.append(neighbour)
        
                elif neighbour == 0:
                    print(neighbour)

from copy import deepcopy
branches = []
explored = set()

def tableDFSRecursiveCaller(table, n):
    
    branch = []
    node = n

    tableDFSRecursive(node, branch, table)
    global branches

    print(branches)


def tableDFSRecursive(node, branch, table):
    global explored

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

sol = Solution().wordBreak(s,wordDict)
# print(sol)