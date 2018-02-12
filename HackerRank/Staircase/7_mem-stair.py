#https://www.python-course.eu/python3_memoization.php

def memoize(f):
    memo={}

    def helper(x):
        if x not in memo:
            memo[x]=f(x)
            print(memo)

        return memo[x]

    return helper


@memoize
def count_paths(n):
    if n == 0:
        return 1
    if n <0:
        return 0

    return count_paths(n-1)+count_paths(n-2)+count_paths(n-3)



s = int(input().strip())
for a0 in range(s):
    n = int(input().strip())
    print(count_paths(n))
