class Solution:

    def __init__(self):
        self.num_courses = 0
        self.adj_matrix = []

        self.explored = set()
        self.clock = -1
        self.post_clock = {}

    def canFinish(self, numCourses, prerequisites):

        self.num_courses = numCourses

        check = self.build_adj(numCourses, prerequisites)
        if not check:
            return False

        check = self.call_dfs()
        if not check:
            return False

        return True
        # asc_postorders = self.sort_postorders()
    

    # def sort_postorders(self):

    #     asc_postorders = [-1]*2*self.num_courses

    #     for i in range(self.num_courses):
    #         asc_postorders[self.post_clock[i]]

    #     return asc_postorders 
    
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
        check = True
        for i in range(self.num_courses):
            if i not in self.explored:
                check = self.dfs(i, check)
        return check

    def dfs(self, node, check):
        
        self.clock+=1
        self.explored.add(node)
        
        for neighbour in range(self.num_courses):
            if self.adj_matrix[node][neighbour]:
                if neighbour in self.explored:
                    return False  
                else:
                    check = self.dfs(neighbour, check)
        
        self.post_clock[node] = self.clock
        self.clock+=1
        return check


numCourses = 2
prerequisites = [[0,1]]

sol = Solution().canFinish(numCourses, prerequisites)
print(sol)