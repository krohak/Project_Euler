import hashlib

memo={}
def memoize(f):
    def helper(*argv):
        hash_nums = hashlib.sha224(str(argv).encode('utf-8')).hexdigest()
        if hash_nums not in memo:
            print('miss')
            memo[hash_nums] = f(argv)
        else:
            print('hit')
        return memo[hash_nums]
    return helper


def putInMemo(*argv):
    hash_nums = hashlib.sha224(str(argv).encode('utf-8')).hexdigest()


@memoize
def productOf(*argv):
    prod = 1
    for arg in argv[0]:
        prod *= arg
    return prod



def main():
    productOf(1,2,3)
    productOf(1,2,3)
    productOf(1,2)

    arr = [12,23,3,4,5]

    size = len(arr)-1

    tup = ()
    for elem in reversed(arr):
        tup_bef = tup
        tup = tup + (elem,)
        # memo(tup) = productOf(tup_bef) * elem

    '''
    traverse array backward
        compute multiplication of right part at each step
        store in memo
    
    traverse forward
        divide into left, skip, right
        compute multiplication of left part using mult of prev left
        lookup right from memo
    '''


if __name__ == "__main__":
    main()

