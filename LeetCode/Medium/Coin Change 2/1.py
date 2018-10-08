import sys


class Solution(object):
    def coinChange(self, coins, amount):

        L = [0 for i in range(amount+1)]

        L[0] = 1


        for i in range(1, amount+1):

            sum_ways = 0

            for coin in coins:

                this_edge = i-coin

                if this_edge >=0:

                    if L[this_edge] >0:
                        sum_ways+=L[this_edge]
                    else:
                        pass
            
            L[i] = sum_ways

        print(L)
        return L[amount]


# coins = [1,2,5]
# amount = 11


# coins = [2]
# amount = 3


# coins = [10]
# amount = 10


coins = [1,2,5]
amount = 5

sol = Solution().coinChange(coins, amount)
print(sol)