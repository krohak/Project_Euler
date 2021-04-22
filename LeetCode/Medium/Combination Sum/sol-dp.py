class Solution:
    
    def combinationSum(self, candidates: list, target: int) -> list:
                
        dp = { k:set() for k in range(target+1) }
        
        for c in candidates:
            if c <= target:
                dp[c].add(tuple([c]))
        
        for t in range(1, target+1):
            for c in candidates:
                if t-c > 0:
                    for tup in dp[t-c]:
                        newTup = tuple(sorted(tup+tuple([c])))
                        if newTup not in dp[t]:
                            dp[t].add(newTup)
                        
        return dp[target]