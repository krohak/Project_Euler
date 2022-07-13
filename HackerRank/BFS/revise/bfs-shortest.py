from collections import defaultdict


class Graph(object):
    def __init__(self,n):
        self.graph = defaultdict(set)
        self.n = n
        self.distances = []

    def connect(self,x,y):
        self.graph[x].add(y)
        self.graph[y].add(x)


    def find_all_distances(self,s):

        distances = [-1 for x in range(self.n)]
        frontier = []
        frontier.append(s)
        explored = set()
        distances[s]=0

        while frontier:
            node = frontier.pop(0)
            explored.add(node)

            for neighbour in self.graph[node]:
                if neighbour not in frontier and neighbour not in explored:
                    frontier.append(neighbour)
                    distances[neighbour]=distances[node]+6

        return(distances)





t = int(input())
for i in range(t):
    n,m = [int(value) for value in input().split()]
    graph = Graph(n)
    for i in range(m):
        x,y = [int(x) for x in input().split()]
        graph.connect(x-1,y-1)
    s = int(input())
    distances=graph.find_all_distances(s-1)
    print(" ".join([repr(x) for x in distances if x != 0]))

