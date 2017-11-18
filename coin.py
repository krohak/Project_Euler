import sys


def memoize(f):
    memo={}
    def helper(x):
        if x not in memo:
            memo[x]=f(x)
            print(memo)
        return memo[x]
    return helper


@memoize
def make_change(n):
    global coins
    #print(n)
    if n<0:
        return 0
    if n==0:
        return 0

    if n in coins:
        return make_change(n-1)+1

    summ=0

    for i in coins:
        for x in range(n):
            


    return summ

n,m = input().strip().split(' ')
n,m = [int(n),int(m)]
coins = [int(coins_temp) for coins_temp in input().strip().split(' ')]
print(make_change(n))
