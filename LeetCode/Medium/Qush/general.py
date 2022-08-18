# Solution 1
def genNEvenFib(N=100):
    prevfx, fx = 1, 1
    i = 0
    while i<N:
        if fx%2==0: i+=1; yield fx
        prevfx, fx = fx, prevfx+fx

assert sum(genNEvenFib(100)) ==  290905784918002003245752779317049533129517076702883498623284700

# Solution 2
def intersection(a, b):
    return list(set(a) & set(b))

assert sorted(intersection([1,2,3,10], [1,3,4,5,6,7,8,9,10])) == [1,3,10]
assert intersection([1,2,3,10], [10]) ==  [10]
assert intersection([10], [1,3]) == []

# Solution 3
def noOdd(n):
    return all( int(c)%2==0 for c in str(n) )

assert noOdd(1121235) == False
assert noOdd(113579) == False
assert noOdd(284) == True

# Solution 4
def repeatingDigitSum(x):
    return sum( int(str(x)*i) for i in range(1,5) )

assert repeatingDigitSum(3) == 3702
assert repeatingDigitSum(5) == 6170