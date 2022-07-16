class Solution(object):
    def minCost(self, costs):
        n  = len(costs)
        for house in range(1, n):
            for color in range(3):
                c1, c2 = set([0,1,2]) - set([color])
                costs[house][color] = min(costs[house-1][c1], costs[house-1][c2]) + costs[house][color]
        return min(costs[n-1])
        