import hashlib

def memoize(f):
    memo={}
    def helper(*argv):
        hash_nums = hashlib.sha224(str(argv).encode('utf-8')).hexdigest()
        if hash_nums not in memo:
            print('miss')
            memo[hash_nums] = f(argv)
        else:
            print('hit')
        return memo[hash_nums]
    return helper


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

