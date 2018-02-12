def memoize(f):
    memo={}
    def helper(x):
        if x not in memo:
            memo[x] = f(x)
        return memo[x]
    return helper


@memoize
def count_steps(n):

    if(n<0):
        return 0

    elif(n==0):
        return 1

    elif(n==1):
        return 1

    elif(n==2):
        return 2

    else:
        return(count_steps(n-1)+count_steps(n-2)+count_steps(n-3))

def count_steps_3(n):

    zero = 1
    one = 1
    two = 2
    total = 0

    for i in range(3,n+1):
        total = zero+one+two
        zero, one, two = one, two, total
    return total

print(count_steps_3(7))
