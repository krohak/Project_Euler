def memoize(f):
    memo = {}
    def helper(x):
        if x not in memo:
            memo[x] = f(x)
            print(memo)
        return memo[x]
    return helper

class Memoize:
    def __init__(self, fn):
        self.fn = fn
        self.memo = {}
    def __call__(self, *args):
        if args not in self.memo:
	           self.memo[args] = self.fn(*args)
        return self.memo[args]

@memoize
#@Memoize
def count_paths(i):
    if i == 0:
        return 1
    if i < 0:
        return 0

    return count_paths(i -1) + count_paths(i-2) + count_paths(i-3)


#count_paths = memoize(count_paths)
print(count_paths(13))




'''def memoize(fn, slot=None, maxsize=32):
    if slot:
        def memoized_fn(obj, *args):
            if hasattr(obj, slot):
                return getattr(obj, slot)
            else:
                val = fn(obj, *args)
                setattr(obj, slot, val)
                # print(val)
                return val
    else:
        @functools.lru_cache(maxsize=maxsize)
        def memoized_fn(*args):
            return fn(*args)

    return memoized_fn
'''
