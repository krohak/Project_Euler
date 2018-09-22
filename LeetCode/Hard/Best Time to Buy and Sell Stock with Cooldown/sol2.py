class Solution:
    def maxProfit(self, prices):

        if not prices:
            return 0

        n = len(prices)

        sell_0 = 0
        sell_1 = 0
        sell_2 = 0

        buy_0 = -prices[0]
        buy_1 = buy_0

        i = 1

        while i < n:

            buy_0 = max( buy_1, sell_2-prices[i] )
            sell_0 = max( sell_1, buy_1+prices[i] )

            
            sell_2 = sell_1

            sell_1 = sell_0
            buy_1 = buy_0

            
            i+=1

        return sell_1

prices = [1,2,3,0,2]
sol = Solution().maxProfit(prices)
print(sol)
