from collections import defaultdict

class Solution:
    def findOrder(self, numCourses: int, prerequisites):
        self.preVisit = [ None for _ in range(numCourses) ] 
        self.postVisit = [ None for _ in range(numCourses) ]
        self.timer = 0
        self.graph = defaultdict(set)
        
        for r1, r2 in prerequisites:
            self.graph[r2].add(r1)
            
        self.visited = set()
        for i in range(numCourses):
            if i not in self.visited:
                self.dfs(i)
        
        for i in range(numCourses):
            for j in self.graph[i]:
                if self.checkBackEdge(i,j): return []
        
        return self.postOrdered(numCourses)
    
    def dfs(self, node):
        self.preVisit[node] = self.timer
        self.timer+=1
        self.visited.add(node)
        for neighbor in self.graph[node]:
            if neighbor not in self.visited:
                self.dfs(neighbor)
        self.postVisit[node] = self.timer
        self.timer+=1
        
    def checkBackEdge(self, i, j):
        return self.preVisit[j] <= self.preVisit[i] and self.postVisit[j] >= self.postVisit[i]

    def postOrdered(self, numCourses):
        sortArr = [ None for _ in range(numCourses*2)]
        for i, time in enumerate(self.postVisit):
            sortArr[time] = i
        return [ i for i in reversed(sortArr) if not i == None ]