class Solution:


    def coinChange(self, coins, original_amount):

        dp = [float('inf') for _ in range(original_amount+1)]
        dp[0] = 0

        for coin in coins:
            if coin < original_amount+1:
                dp[coin] = 1

        for amount in range(1, original_amount+1):
            min_ways = float('inf')
            for coin in coins:
                
                if (amount-coin) >= 0:
                    ways = dp[amount-coin]+1
            
                    min_ways = min(min_ways, ways)
            
            dp[amount] = min_ways
        
        ways = dp[original_amount]
        return ways if not ways==float('inf') else -1


coins = [2]
amount = 3


# coins = [1, 2, 5]
# amount = 100

coins = Solution().coinChange(coins, amount)
print(coins)