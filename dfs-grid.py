import hashlib

def getBiggestRegion(grid,n,m):
    #call dfs for all nodes
    largest_region=0
    for x in range(n):
        for y in range(m):
            if grid[x][y] == 1:
                #print(x,y)
                region = dfs([x,y],grid,n,m)
                if region>largest_region:
                    largest_region=region

    return largest_region



def memoize(f):
    memo = {}
    def helper(x,n,m):
        has=hashlib.sha224(str(x).encode('utf-8')).hexdigest()
        if has not in memo:
            memo[has] = f(x,n,m)
            #print(x,memo)

        return memo[has]

    return helper


@memoize
def neighbours(node,n,m):
    #check if active neighbours exist
    active=[]
    for x in range(-1,2):
        for y in range(-1,2):
            a = node[0] + x
            b = node[1] + y
            
            if (a >= 0 and a < n and b>=0 and b < m):
                if(not a == node[0] or not b == node[1]):
                    if grid[a][b] == 1:
                        active.append([a,b])
    return active



def dfs(node,grid,n,m):
    explored = set()
    region = 1

    def recursive_dls(node,grid,explored,region):
        if not neighbours(node,n,m):
            return region

        explored.add(hashlib.sha224(str(node).encode('utf-8')).hexdigest())


        for neighbour in neighbours(node,n,m):
            if (hashlib.sha224(str(neighbour).encode('utf-8')).hexdigest()) not in explored:
                region = recursive_dls(neighbour,grid,explored,region)
                region+=1
                
        return region

    region = recursive_dls(node,grid,explored,region)
    return region



n = int(input().strip())
m = int(input().strip())
grid = []
for grid_i in range(n):
    grid_t = list(map(int, input().strip().split(' ')))
    grid.append(grid_t)
#print(grid[0][0])
print(getBiggestRegion(grid,n,m))

