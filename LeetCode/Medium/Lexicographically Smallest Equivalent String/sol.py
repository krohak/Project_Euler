from collections import defaultdict

class Solution(object):
    def __init__(self):
        self.graph = defaultdict(list)
        self.char2cc = {}

    def buildGraph(self, s1, s2):
        for c1, c2 in zip(s1,s2):
            self.graph[c1].append(c2)
            self.graph[c2].append(c1)

    def findConnectedComponents(self):
        self.explored = set()
        cc = 0
        for o in range(ord('a'), ord('z')+1):
            if chr(o) not in self.explored:
                self.dfs(chr(o), cc)
                cc+=1

    def dfs(self, ltr, cc):
        self.explored.add(ltr)
        self.char2cc[ltr] = cc
        for neighbor in self.graph[ltr]:
            if neighbor not in self.explored:
                self.dfs(neighbor, cc)

    def smallestEquivalentString(self, s1, s2, baseStr):
        self.buildGraph(s1, s2)
        self.findConnectedComponents()
        self.cc2chars = defaultdict(list)
        for let, cc in self.char2cc.items(): 
            self.cc2chars[cc].append(let)
        return ''.join([ min(self.cc2chars[self.char2cc[let]]) for let in baseStr ])

s1 = "parker"
s2 = "morris" 
baseStr = "parser"

s1 = "hello" 
s2 = "world" 
baseStr = "hold"

s1 = "leetcode" 
s2 = "programs" 
baseStr = "sourcecode"
print(Solution().smallestEquivalentString(s1, s2, baseStr))