def makeChangeDP(amount):

    coins = [1,3,5]

    L = [0 for i in range(amount+1)]

    for i in range(1,amount+1):

        min_coins = amount
        for coin in coins:

            if i-coin >=0:

                coins_reqd = L[i-coin]+1
                if min_coins > coins_reqd:
                    min_coins = coins_reqd
        
        L[i] = min_coins

    
    return L[amount]


sol  = makeChangeDP(20)
print(sol)