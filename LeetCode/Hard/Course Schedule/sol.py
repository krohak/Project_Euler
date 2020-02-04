class Solution:

    def __init__(self):
        self.num_courses = 0
        self.adj_matrix = []

        self.explored = set()
        self.clock = 0
        self.pre_clock = {}
        self.post_clock = {}

    def canFinish(self, numCourses, prerequisites):

        self.num_courses = numCourses

        if not self.build_adj(numCourses, prerequisites):
            return False
            
        self.call_dfs()

        if not self.check_backedges():
            return False

        return True

    def check_backedges(self):

        for from_node in range(self.num_courses):
            for to_node in range(self.num_courses):
                if self.adj_matrix[from_node][to_node]:
                    if self.pre_clock[to_node] < self.pre_clock[from_node] and self.post_clock[to_node] > self.post_clock[from_node]:
                        return False
        return True
    
    def build_adj(self, numCourses, prerequisites):
        adj_matrix = []
        for _ in range(numCourses):
            nest = []
            for _ in range(numCourses):
                nest.append(0)
            adj_matrix.append(nest)
        self.adj_matrix = adj_matrix

        for req in prerequisites:
            to_node, from_node = req[0], req[1]
            if from_node > self.num_courses or to_node > self.num_courses:
                return False
            self.adj_matrix[from_node][to_node] = 1
        return True

    def call_dfs(self):
        for i in range(self.num_courses):
            if i not in self.explored:
                self.dfs(i)

    def dfs(self, node):
        
        self.pre_clock[node] = self.clock
        self.clock+=1
        
        self.explored.add(node)
        
        for neighbour in range(self.num_courses):
            if self.adj_matrix[node][neighbour] and neighbour not in self.explored:
                self.dfs(neighbour)
        
        self.post_clock[node] = self.clock
        self.clock+=1
        


numCourses = 2
prerequisites = [[0,1],[1,0]]

sol = Solution().canFinish(numCourses, prerequisites)
print(sol)