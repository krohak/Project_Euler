from collections import defaultdict
def Graph(object):
    def __init__(self,n):
        self.edges=defaultdict(set)
        self.n=n
        self.distances=[]

    def connect(x,y):
        self.edges[x].add(y)
        self.edges[y].add(x)

    def bfs(self, initial):

        frontier=[]
        explored=set()

        frontier.append(node)

        while(frontier):

        node = frontier.pop(0)
        explored.add(node)

            for neighbour in self.edges[node]:
                if neighbour not in explored and neighbour not in frontier:
                    frontier.append(neighbour)


    def call_dfs(self,initial):
        explored=set()
        dfs(initial)

    def dfs(self, initital):

        if not self.edges[initial]:
            return

        explored.add(initital)

        for neighbour in self.edges[node]:
            if neighbour not in explored:
                dfs(neighbour)
        return
