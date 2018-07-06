from hashlib import sha224

memo={}
def handleMemo(tup):
    tup_str = str(tup).encode('utf-8')
    hash_nums = sha224(tup_str).hexdigest()
    if hash_nums not in memo:
        # print('miss',tup,memo)
        if len(tup) == 0:
            memo[hash_nums] = 1
        elif len(tup) == 1:
            memo[hash_nums] = tup[0]
        else:
            # pop = 
            memo[hash_nums] = handleMemo(tup[:-1]) * tup[-1]
    else:
        pass
        # print('hit',tup,memo)
    return memo[hash_nums]

'''
traverse array backward
    compute multiplication of right part at each step using mult of prev right
    store in memo
'''
def goBack(arr):
    tup = ()
    back_products = []
    for elem in reversed(arr):
        tup = tup + (elem,)
        back_products.append(handleMemo(tup))

    return back_products


'''
traverse forward
    compute multiplication of left part using mult of prev left
    lookup right from memo
'''
def goForward(arr):
    tup = ()
    fow_products = []
    for elem in arr:
        tup = tup + (elem,)
        fow_products.append(handleMemo(tup))

    return fow_products

def main():
    
    arr = [12,23,3,4,5]

    back_products = goBack(arr)
    print(back_products)
    fow_products = goForward(arr)
    print(fow_products)

    back_products.pop()
    fow_products.pop()

    back_products = [1] + back_products
    fow_products = [1] + fow_products

    print(fow_products)
    print(back_products)
    
    size = len(back_products)

    answer = []
    for i in range(size):
        answer.append(fow_products[i]*back_products[size-1-i])

    print(answer)


if __name__ == "__main__":
    main()

