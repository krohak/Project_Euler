
from copy import deepcopy

def merge_sort(nums):

    n = len(nums)

    if n == 1:
        return nums

    nums_left = deepcopy(nums[:n//2])
    nums_right = deepcopy(nums[n//2:])

    nums_left_sorted = merge_sort(nums_left)
    nums_right_sorted = merge_sort(nums_right)

    ans = []
    i = 0
    j = 0

    while i < n//2 and j < n-(n//2):
        if nums_left_sorted[i] <= nums_right_sorted[j]:
            ans.append(nums_left_sorted[i])
            i+=1
        else:
            ans.append(nums_right_sorted[j])
            j+=1

    while i<n//2:
        ans.append(nums_left_sorted[i])
        i+=1
    
    while j<n-(n//2):
        ans.append(nums_right_sorted[j])
        j+=1

    return ans


arr = [3,6,10,2,7,4,5,9,1,8]
arr =  [1,1,1,0,0,0,0]
arr = [3,6,10,2,7,4,5,9,1,8,3,6,10,2,7,4,5,9,1,8]

ans = merge_sort(arr)
print(ans)