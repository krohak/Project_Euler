def coins_dp(coins, amount):

    if not amount:
        return 0

    amounts_list = [ float("inf") for i in range(amount+1) ]

    for coin in coins:
        if coin <= amount:
            amounts_list[coin] = 1
    
    print(amounts_list)
    
    for (target, _) in enumerate(amounts_list):
        min_coins = float("inf")
        for coin in coins:
            if (target-coin>0):
                min_coins = min(min_coins, amounts_list[target-coin] + 1)

        amounts_list[target] = min(min_coins, amounts_list[target]) 
    
    print(amounts_list)
    
    if amounts_list[-1] == float("inf"):
        return -1
    return amounts_list[-1]



coins = [1, 2, 5]
amount = 11

coins = [2] 
amount = 3

coins = [1] 
amount = 0

coins = [2] 
amount = 1

coins = [1] 
amount = 1
 
 
min_coins = coins_dp(coins, amount)
print(min_coins)