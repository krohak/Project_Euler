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

    def bfs(self, root):

        frontier = []
        explored = set()

        frontier.append(root)

        while frontier:

            node = frontier.pop(0)
            explored.add(node)


            for neighbour in self.edges[node]:
                if not neighbour in frontier and not neighbour in explored:
                    frontier.append(neighbour)

    
    def bfs_parents(self, root):
        frontier = []
        explored = set()
        parents = {}

        frontier.append(root)
        parents[root] = 0

        while frontier:

            node = frontier.pop(0)
            explored.add(node)


            for neighbour in self.edges[node]:
                if not neighbour in frontier and not neighbour in explored:
                    frontier.append(neighbour)
                    parents[neighbour] = node

        print(parents)

    
    def bfs_detect_cycles(self, root):

        frontier = []
        explored = set()
        parents = {}

        frontier.append(root)
        parents[root] = 0

        while frontier:
            node = frontier.pop(0)
            explored.add(node)

            for neighbour in self.edges[node]:
                if not neighbour in explored and not neighbour in frontier:
                    frontier.append(neighbour)
                    parents[neighbour] = node
                elif parents[neighbour] != node and not neighbour in explored:
                    print("Cycle detected from {} to {} through {}".format(node, neighbour, parents[neighbour]))

graph = Graph(10)
graph.connect(1,2)
graph.connect(2,3)
graph.connect(3,4)
graph.connect(1,3)

# print(graph.edges)
graph.bfs_detect_cycles(1)