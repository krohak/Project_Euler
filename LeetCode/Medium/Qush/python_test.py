# Solution 1
generateMultiples = lambda n,x: (i for i in range(x, n+1, x) )
# sum of all positive integers strictly less than 102030 which are divisible by 3
assert sum(generateMultiples(102029, 3)) == 1734969135
# sum of all positive integers up to and including 102030 which are divisible by 3
assert sum(generateMultiples(102030, 3)) == 1735071165

# Solution 2
def listOfNLists(n):
    return [ list(range(1, x+1)) for x in range(1, n+1) ]

assert listOfNLists(3) == [[1], [1, 2], [1, 2, 3]]
assert listOfNLists(2) == [[1], [1, 2]]
assert listOfNLists(0) == []