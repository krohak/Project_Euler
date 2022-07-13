class Solution(object):
    def coinChange(self, coins, amount):
        dp = [ float('inf') for _ in range(amount+1) ]
        dp[0] = 0
        for x in range(1, amount+1):
            dp[x] = min([ dp[x-coin] for coin in coins if x-coin>=0 ] or [float('inf')]) + 1
        return dp[amount] if dp[amount]!=float('inf') else -1