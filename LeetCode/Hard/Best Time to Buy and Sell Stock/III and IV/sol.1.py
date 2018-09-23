from sys import maxsize

class Solution(object):
    
    def maxProfit(self, k, prices):

        if not prices:
            return 0

        n = len(prices)


        if(n==0 or n==1 or k == 0): 
            return 0

        if (k > n/2):
            ans = 0
            for i in range(1,n):
                ans += max(prices[i] - prices[i-1],0)
                
            return ans
            
        
        sell = {}
        buy = {}
        
        for i in range(n+1):
            for transaction in range(k+1):
                sell[(i,transaction)] = 0
                buy[(i,transaction)] = 0
        
        
        for transaction in range(1,k+1):
            buy[(0,transaction)] = -maxsize-1

        for i in range(1, n+1):
            for transaction in range(1,k+1):
                buy[(i,transaction)] = max( (buy[(i-1, transaction)]) , (sell[(i-1, transaction-1)]-prices[i-1]) )
                sell[(i,transaction)] = max( (buy[(i-1, transaction)]+prices[i-1]) , (sell[(i-1, transaction)]) )



#         for i in range(1,n+1):
#             for transaction in range(1,k+1):
#                 print(i, transaction, sell[(i,transaction)])
        
#         for i in range(1,n+1):
#             for transaction in range(1,k+1):
#                 print(i, transaction, buy[(i,transaction)],)

        return sell[(n,k)]