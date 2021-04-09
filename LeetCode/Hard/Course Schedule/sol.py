class Solution:
    
    def __init__(self):
        self.explored = set()
        self.previsit = []
        self.postvisit = []
        self.clock = 0
        
    def canFinish(self, numCourses, prerequisites):
        self.courseGraph = { n:[] for n in range(numCourses) }
        for c1, c2 in prerequisites: self.courseGraph[c1].append(c2)
        self.previsit = [ None for _ in range(numCourses) ]
        self.postvisit = [ None for _ in range(numCourses) ]
        
        for c in range(numCourses):
            if c not in self.explored:
                self.dfs(c)
        
        for c, neighbours in self.courseGraph.items():
            for n in neighbours:
                if self.checkBackEdge(c, n): return False
        
        return True
                
    def dfs(self, c):
        self.explored.add(c)
        self.previsit[c] = self.clock
        self.clock +=1
        for n in self.courseGraph[c]:
            if n not in self.explored:
                self.dfs(n)
        self.postvisit[c] = self.clock
        self.clock +=1

    def checkBackEdge(self, c, n):
        if self.previsit[n] <= self.previsit[c] and self.postvisit[c] <= self.postvisit[n]:
            return True
        return False