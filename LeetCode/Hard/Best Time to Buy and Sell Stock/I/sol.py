class Solution(object):

    def maxProfit(self, prices):

        if not prices:
            return 0

        sell_price = prices[0]

        max_profit = 0

        for i in range(1, len(prices)):

            profit = prices[i] - sell_price

            if profit > max_profit:
                max_profit = profit

            if prices[i] < sell_price:
                sell_price = prices[i]

        return max_profit


prices = [7, 1, 5, 3, 6, 4]
sol = Solution().maxProfit(prices)
print(sol)
