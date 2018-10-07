memo = {}

def makeChangeCaller(amount):

    coins = [1,3,5]
    return makeChange(amount,coins)


def makeChange(amount, coins):

    if amount == 0:
        return 0
    
    global memo
    if amount in memo:
        return memo[amount]

    min_coins = amount
    for coin in coins:
        this_amount = amount-coin

        if this_amount>=0:
            this_coins = makeChange(this_amount, coins)
            this_coins+=1

            if this_coins < min_coins:
                min_coins = this_coins
    
    memo[amount] = min_coins
    return min_coins


sol = makeChangeCaller(20)
print(sol)
print(memo)