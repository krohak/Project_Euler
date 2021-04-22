class Solution:
    def __init__(self):
        self.combinations = []
        self.n = 0
    
    def generateParenthesis(self, n: int) -> list:
        self.n = n
        self.dfs(0, 0, "")
        return self.combinations
        
    def dfs(self, numOpen, numClosed, pString):
        
        if len(pString)==2*self.n:
            self.combinations.append(pString)
            return
        
        if numOpen < self.n:
            self.dfs(numOpen+1, numClosed, pString+'(')
        
        if numClosed < numOpen:
            self.dfs(numOpen, numClosed+1, pString+')')