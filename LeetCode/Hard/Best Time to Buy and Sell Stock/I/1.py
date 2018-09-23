class Solution(object):

    def maxProfit(self, prices):

        if not prices:
            return 0

        L = [0 for price in prices]
        n = len(prices)

        for j in range(n):
            max_profit = 0
            for i in range(0, j):
                profit = prices[j] - prices[i]
                if profit > max_profit:
                    max_profit = profit

            L[j] = max_profit

        return max(L)


prices = [7, 1, 5, 3, 6, 4]
sol = Solution().maxProfit(prices)
print(sol)
