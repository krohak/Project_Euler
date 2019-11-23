def coins_dp(amount, coins):

    ways_list = [ 0 for target in range(amount+1) ]
    ways_list [0] = 1

    for coin in coins:

        for target in range(amount+1):

            if (target-coin)>=0:
                ways_list[target]+=ways_list[target-coin]

    return ways_list[-1]

amount = 5
coins = [1, 2, 5]
num_ways = coins_dp(amount, coins)
print(num_ways)