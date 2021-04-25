class Solution:
    def generate(self, numRows: int) -> list:
        pascalTri = [[1]]
        
        for i in range(1, numRows):
            
            curLevel = [ 1 for _ in range(i+1)]
            pastLevel = pascalTri[-1]
            
            for j in range(1, i):
                curLevel[j] = pastLevel[j-1]+pastLevel[j]
            
            pascalTri.append(curLevel)
        
        return pascalTri