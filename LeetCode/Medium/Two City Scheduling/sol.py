class Solution:
    def twoCitySchedCost(self, costs):
        
        costs_sorted = [ (cost_pair[0]-cost_pair[1], cost_pair[0], cost_pair[1]) for   cost_pair in costs ]
        
        costs_sorted.sort()
        
        ans = 0
        n = len(costs)//2
        
        for i in range(n):
            ans+=costs_sorted[i][1]
        
        for i in range(n,2*n):
            ans+=costs_sorted[i][2]
            
        return ans