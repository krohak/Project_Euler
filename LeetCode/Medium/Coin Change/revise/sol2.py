class Solution(object):
    def coinChange(self, coins, amount):
        
        if not amount:
            return 0

        L = [ float('inf') for _ in range(0, amount+1)]
        
        
        for coin in coins:
            if coin <= amount:
                L[coin] = 1
            
        
        for target in range(1, amount+1):
            
            fewest = float('inf')
            for coin in coins:
                
                if target-coin > 0:
                    num_coins = L[target-coin] + 1        
                    fewest = min(num_coins, fewest)
            
            L[target] = min(L[target], fewest)
        
        
        return -1 if L[amount] == float('inf') else L[amount]