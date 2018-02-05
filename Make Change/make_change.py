#!/bin/python3

import sys



def get_num(n,coins,index,memo):

    if(n==0):
        return 1

    if(index >= len(coins)):
        return 0

    if(memo.get((n,index))):
        return memo[(n,index)]

    amountwithcoin = 0
    ways = 0

    while(amountwithcoin <= n):
        remaining = n - amountwithcoin
        ways += get_num(remaining,coins,index+1,memo)
        amountwithcoin += coins[index]

    memo[(n,index)] = ways
    return ways

def make_change(coins, n):
    memo={}
    return get_num(n,coins,0,memo)


n,m = input().strip().split(' ')
n,m = [int(n),int(m)]
coins = [int(coins_temp) for coins_temp in input().strip().split(' ')]
print(make_change(coins, n))
