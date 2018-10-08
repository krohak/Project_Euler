
class Solution(object):
    def coinChange(self, coins, amount):

        if amount ==0:
            return 0

        L = [0 for i in range(amount+1)]

        L[0] = 1


        for coin in coins:

            for i in range(coin,amount+1):
                
                if i-coin>=0:
                    L[i] += L[i-coin]

        print(L)
        return L[amount]


coins = [1,2,5]
amount = 11


# coins = [2]
# amount = 3


# coins = [10]
# amount = 10


# coins = [1,2,5]
# amount = 5

sol = Solution().coinChange(coins, amount)
print(sol)