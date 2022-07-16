class Solution(object):
    def minCost(self, costs):
        n  = len(costs)
        dp = [ [float('inf')]*3 for h in range(n) ]
        for color in range(3):   
            dp[0][color] = costs[0][color]
        
        for house in range(1, n):
            for color in range(3):
                c1, c2 = set([0,1,2]) - set([color])
                dp[house][color] = min(dp[house-1][c1], dp[house-1][c2]) + costs[house][color]
                
        return min(dp[n-1])

# [     r    b    g
#     [17, 2, 17], h1
#     [18, 33, 7], h2
#     [21, 10, 37]  h3
# ]
        
# cost[0][0] -/> cost[1][0]
#            ->  cost[1][1]
#            ->  cost[1][2]


# cost[0][1]  
# cost[0][2]



# min(cost[n-1])

# h1 -> 1 1 100
# h2 -> 2 200 200
# h3 -> 1 1 1