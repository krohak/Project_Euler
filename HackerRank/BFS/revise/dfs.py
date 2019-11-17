from collections import defaultdict

class Graph(object):
    def __init__(self,n):
        self.edges=defaultdict(set)
        self.n=n
        self.distances=[]
        self.nodes=set()

    def connect(self,x,y):
        self.edges[x].add(y)
        self.edges[y].add(x)
        self.nodes.add(x)
        self.nodes.add(y)


    def dfs_caller(self, root):
        explored = set()
        
        for node in self.nodes:
            if node not in explored:
                self.dfs(node, 0, explored)

        
         

    
    def dfs(self, root, parent, explored):
        explored.add(root)
        print(root, parent)

        for neighbour in self.edges[root]:
            if not neighbour in explored:
                self.dfs(neighbour, root, explored)




graph = Graph(10)
graph.connect(1,2)
# graph.connect(2,3)
graph.connect(3,4)
graph.connect(1,3)
graph.connect(5,3)
graph.connect(5,4)

# print(graph.edges)
graph.dfs_caller(1)