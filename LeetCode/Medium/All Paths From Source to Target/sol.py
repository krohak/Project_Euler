from copy import deepcopy

class Solution:
    
    
    def __init__(self):
        
        self.n = 0
        self.graph = []     
        
        self.paths = []
    
    
    def allPathsSourceTarget(self, graph):
        
        
        self.n = len(graph)
        self.graph = graph
        
        self.dfs_caller()
        
        return self.paths
    
    
    def dfs_caller(self):
        path = []
        self.dfs(0, path)
        
    
        
    def dfs(self, node, path):
        
        path_deep = deepcopy(path)
        path_deep.append(node)
        
        if node == self.n-1:
            self.paths.append(path_deep)
            return 
    
        
        for neighbour in self.graph[node]:
            self.dfs(neighbour, path_deep)