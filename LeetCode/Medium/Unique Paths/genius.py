class Solution(object):
    def uniquePaths(self, m, n):
        """
	creates a mfkin gradient
        """
        vec = [1] * m
        
        for i in range(1,n):
            for j in range(1, m):
                vec[j] += vec[j-1]
                
        return vec[-1] 
