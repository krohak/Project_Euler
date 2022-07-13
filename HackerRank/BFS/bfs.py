class Solution:
    def __init__(self):
        self.parents = {}
        self.frontier = []
        self.explored = set()
        self.graph = {
            0: [1],
            1: [2, 4],
            2: [1, 3],
            3: [1, 2],
            4: [1]
        }

    def bfs(self, start, end):
        self.frontier.append(start)
        while self.frontier:
            node = self.frontier.pop(0)
            if node == end: return self.parents
            self.explored.add(node)
            for neighbor in self.graph[node]:
                if not neighbor in self.explored and not neighbor in self.frontier:
                    self.frontier.append(neighbor)
                    self.parents[neighbor] = node
        return self.parents

start, end = 0, 3
parentDict = Solution().bfs(0, 3)
path = [end]
while parentDict[end]:
    path.append(parentDict[end])
    end = parentDict[end]
print(list(reversed(path)))