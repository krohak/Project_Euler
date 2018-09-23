class Solution(object):
    
    def maxProfit(self, k, prices):

        if not prices:
            return 0

        n = len(prices)+1
        
        sell = {}
        buy = {}
        
        for i in range(n):
            for transaction in range(0,k+1):
                sell[(i,transaction)] = 0
                buy[(i,transaction)] = 0

        
        buy[(0,0)] = -prices[0]
        
        for i in range(1, n):

            for transaction in range(1,k+1):
                
                # sell[(i,transaction)] = max( sell[(i-1, transaction)], buy[ (i-1, transaction-1) ]+prices[i])
                # buy[(i,transaction-1)] = max( buy[(i-1, transaction-1) ], sell[ (i-1, transaction-1) ]-prices[i] )

                buy[(i,transaction)] = max( buy[(i-1, transaction)], sell[(i-1, transaction-1)]-prices[i-1] )
                sell[(i,transaction)] = max( sell[(i-1, transaction)], buy[(i-1, transaction)]+prices[i-1] )
                
                   
                # sell[i][j] = max( sell[i-1][j], buy[i-1][j]+prices[i-1])
                # buy[i][j] = max( buy[i-1][j] , sell[i-1][j-1] - prices[i-1])
        

        for i in range(1,n):
            for transaction in range(1,k+1):
                print(i, transaction, sell[(i,transaction)])
        
        for i in range(1,n):
            for transaction in range(1,k+1):
                print(i, transaction, buy[(i,transaction)],)

        # print("SELL: ", sell)
        # print("BUY: ", buy)

        return sell[(n-1,k)]
        
        


prices = [7, 1, 5, 3, 6, 4]
prices = [3,3,5,0,0,3,1,4]
# prices = [1,2,3,4,5]
# prices = [7,6,4,3,1]

sol = Solution().maxProfit(2,prices)
print(sol)
