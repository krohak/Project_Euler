from copy import deepcopy

class Solution:
    def __init__(self):
        self.answer = []
        self.candidates = []
        self.target = 0
        self.explored = set()
    
    def combinationSum(self, candidates: list, target: int) -> list:
        self.candidates = candidates
        self.target = target
        
        self.dfs([])
        
        return self.answer
        
    def dfs(self, curList):
        
        if sum(curList) > self.target:
            return
        
        elif sum(curList) == self.target and tuple(sorted(curList)) not in self.explored:
            self.answer.append(curList)
            self.explored.add(tuple(sorted(curList)))
            return
                
        for c in self.candidates:
            curListCopy = deepcopy(curList)
            curListCopy.append(c)
            self.dfs(curListCopy)