'''
#[1110]^n=[F(n+1)F(n)F(n)F(n−1)] .

import numpy as np

res=0

a=np.array([[1,1],[1,0]])
b=np.array([[1,1],[1,0]])

while b[0][1]<4000000:
    b=np.dot(b,a)
    if b[0][1]%2==0:
        res+=b[0][1]

print(res)
print(b[1][1])
'''

def memoize(f):
    memo={}
    def helper(n):
        if n not in memo:
            memo[n] = f(n)
        return memo[n]
    return helper


@memoize
def fibonacci(n):
    if n==0:
        return 0
    if n==1:
        return 1

    return (fibonacci(n-1)+ fibonacci(n-2))


n = int(input())
print(fibonacci(n))
