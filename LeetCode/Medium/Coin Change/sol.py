import sys


class Solution(object):
    def coinChange(self, coins, amount):

        L = [-1 for i in range(amount+1)]

        L[0] = 0


        for i in range(1, amount+1):

            min_coins = sys.maxsize
            for coin in coins:

                this_edge = i-coin
                if this_edge >= 0:

                    if L[this_edge] <0:
                        pass
                    else:
                        if L[this_edge] < min_coins:
                            min_coins = L[this_edge]
            
            if min_coins==sys.maxsize:
                L[i] = -1
            else:
                L[i] = min_coins+1
        
        # print(L)
        return L[amount]


coins = [1,2,5]
amount = 11


coins = [2]
amount = 3

sol = Solution().coinChange(coins, amount)
print(sol)