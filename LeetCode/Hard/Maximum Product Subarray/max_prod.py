def maxProduct(nums):
    
    if not len(nums):
        return 0
    
    num_len = len(nums)
    max_prod = nums[0]

    window_size = 0
    while window_size < num_len:
        pos = 0
        while pos+window_size < num_len:
            prod = helper(tuple(nums[pos:pos+window_size+1]))
            if prod > max_prod:
                max_prod = prod

            pos+=1
        window_size+=1

    return max_prod
        
memo = {}       
def helper(indices):
    if len(indices) == 1:
        memo[indices] = indices[0]

    else:
        memo[indices] = memo[indices[:-1]]*indices[-1]

    return memo[indices]

nums = [2,3,-2,4]
# nums = [-2,0,-1]
max_prod = maxProduct(nums)

print(max_prod)