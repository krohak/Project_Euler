class Solution(object):
    def uniquePaths(self, m, n):        
        return unique_paths(m,n)
    

def memoize(f):
    memo={}
    
    def helper(x,y):
        if (x,y) not in memo:
            memo[(x,y)] = f(x,y)
        return memo[(x,y)]
    
    return helper

@memoize
def unique_paths(m,n):
    if(m==1 or n==1):
        return 1
    
    return(unique_paths(m-1,n) + unique_paths(m,n-1))
