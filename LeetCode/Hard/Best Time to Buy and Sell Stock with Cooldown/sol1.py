class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices:
            return 0
        n = len(prices)
        sell = [0 for i in range(n)]
        buy = [0 for i in range(n)]
        buy[0] = -prices[0]
        
        for i in range(1, n):
            sell[i] = max(sell[i-1], buy[i-1]+prices[i])
            buy[i] = max(buy[i-1], sell[i-2]-prices[i] if i-2>=0 else -prices[i])
        return sell[n-1]