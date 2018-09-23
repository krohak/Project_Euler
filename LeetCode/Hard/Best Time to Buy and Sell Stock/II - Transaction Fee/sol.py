class Solution(object):
    
    def maxProfit(self, prices, fee):

        if not prices:
            return 0

        n = len(prices)
        
        sell_1 = 0
        buy_1 = -prices[0]
        
        for i in range(1, n):
            
            sell_0 = max( sell_1, buy_1+prices[i]-fee )
            buy_0 = max( buy_1, sell_1-prices[i] )

            sell_1 = sell_0
            buy_1 = buy_0

        return sell_1