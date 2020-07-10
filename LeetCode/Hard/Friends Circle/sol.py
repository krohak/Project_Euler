class Solution:
    def __init__(self):
        self.circles = 0
        self.matrix = []
        
        self.N = 0
        
        self.explored = set()
    
    def findCircleNum(self, M):
    
        self.matrix = M
        
        self.N = len(self.matrix)
        
        if self.N==0:
            return 
        
        for node in range(self.N):
            if node not in self.explored:
                self.circles+=1
                self.dfs(node)
                    
        return self.circles
                
    
    def dfs(self, node):
        self.explored.add(node)
        
        for neighbour in self.get_neighbours(node):
            if neighbour not in self.explored:
                self.dfs(neighbour)
         
    
    def get_neighbours(self, node):
        return [node for node, state in enumerate(self.matrix[node]) if state]
        
        
        