from copy import deepcopy

class Solution:
    
    
    def __init__(self):
        
        
        self.n = 0
        self.graph = []
        
        self.explored = set()
        
        self.paths = []
    
    
    def allPathsSourceTarget(self, graph):
        
        
        self.n = len(graph)
        self.graph = graph
        
        self.dfs_caller()
        
        return self.paths
    
    
    def dfs_caller(self):
        for i in range(self.n):
            if i not in self.explored:
                path = []
                self.dfs(i, path)
        
    
        
    def dfs(self, node, path):
        
        path_deep = deepcopy(path)
        path_deep.append(node)
        
        self.explored.add(node)
        
        for neighbour in self.graph[node]:
            if neighbour not in self.explored:
                
                if neighbour == self.n-1:
                    path_deep.append(neighbour)
                    self.paths.append(path_deep)

                else:
                    self.dfs(neighbour, path_deep)