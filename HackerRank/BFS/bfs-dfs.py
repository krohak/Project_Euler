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

    def bfs(self, node):
        frontier=[]
        explored=set()

        frontier.append(node)

        while(frontier):
            node = frontier.pop(0)
            explored.add(node)
            for neighbour in self.edges[node]:
                if neighbour not in explored and neighbour not in frontier:
                    frontier.append(neighbour)


    def call_dfs(self):
        explored=set()
        for node in self.nodes:
            if node not in explored:
                self.dfs(node, explored)

    def dfs(self, initial, explored):
        # if not self.edges[initial]:
        #     return
        explored.add(initial)
        for neighbour in self.edges[initial]:
            if neighbour not in explored:
                self.dfs(neighbour, explored)
        return
