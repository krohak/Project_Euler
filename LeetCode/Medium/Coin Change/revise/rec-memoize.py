# def memoize(f):
#     memo = {}
#     def helper(x):
#         if x not in memo:
#             memo[x] = f(x)
#             print(memo)
#         return memo[x]
#     return helper

class Solution:

    def __init__(self):
        self.coins = []
        self.memo = {}


    def coinChange(self, coins, amount):

        self.coins = coins
        num_coins = self.rec_coins(amount)
        return -1 if num_coins==float('inf') else num_coins
    

    def rec_coins(self, amount):

        if amount in self.memo:
            return self.memo[amount]

        if amount < 0:
            return float('inf')
        
        if amount == 0:
            return 0

        
        min_coins = float('inf')
        for coin in self.coins:
            num_change = self.rec_coins(amount-coin) + 1
            min_coins = min(min_coins, num_change)

        self.memo[amount] = min_coins

        return min_coins



# coins = [1, 2, 5]
# amount = 100

coins = [2]
amount = 3

coins = Solution().coinChange(coins, amount)
print(coins)