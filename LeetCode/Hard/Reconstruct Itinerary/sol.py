from collections import defaultdict

class Solution:
    
    def __init__(self):
        self.graph = defaultdict(lambda: defaultdict(int))
        self.itinerary = []
    
    def findItinerary(self, tickets: list) ->list:
        
        for start, end in tickets:
            self.graph[start][end]+=1
        
        self.dfs("JFK")
        
        return self.itinerary[::-1]
        
    def dfs(self, node):
        
        sortedNeighbours = sorted(self.graph[node].keys())
        for n in sortedNeighbours:
            if self.graph[node][n] > 0:
                self.graph[node][n]-=1
                self.dfs(n)
                
        self.itinerary.append(node)
        