import sys

memo = {}

def makeChangeCaller(amount):
    
    # n = len(coins)
    coins = [1,3,5]
    coin_count = 0
    
    num_coins = makeChange(coins, amount, coin_count)
    
    return num_coins
    
    
def makeChange(coins, amount, coin_count):
    
    global memo
    
    min_num_coins = amount

    for coin in coins:
        
        if amount-coin>=0:
            if (amount-coin) in memo:
                num_coins = memo[(amount-coin)]

            num_coins = makeChange(coins,amount-coin,coin_count+1)
            if num_coins < min_num_coins:
                min_num_coins = num_coins
        else:
            return coin_count
        

    memo[(amount-coin)] = min_num_coins

        
    return min_num_coins
        
        
# for line in sys.stdin:
    
#     num_coins = makeChangeCaller(int(line))
#     print(num_coins, end="")


sol = makeChangeCaller(20)
print(sol)
print(memo)            