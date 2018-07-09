'''
Notes:
1. Use array as its own frequency array by placing num at its own index
2. largest num in nums (if nums is a perfect sequence) can be len(nums)
3. We can always use -1 to mark stuff when doing in-place calculations
4. gfg divides neg+0 and pos, traverses through pos nums and marks -1. Then from 0 to size, return i if nums[i]>0
- https://www.geeksforgeeks.org/find-the-smallest-positive-number-missing-from-an-unsorted-array/
- https://www.geeksforgeeks.org/?p=9755
- https://www.geeksforgeeks.org/?p=7953
''' 
def firstMissingPositive(nums):

    length = len(nums)
    i = 0 
    nums.append(-1) # in case the missing positive is len(nums)+1
    
    while(i < length):
        if nums[i] == i: # if index equal to number at index
            i = i +1 # go to next (sorted)
        elif nums[i] <0: # dont care about negatives
            i = i +1
        elif nums[i] > length: # dont care about huge numbers (>len of nums)
            i = i +1
        else: # if not sorted, not a negative or a big number
            tmp = nums[nums[i]]
            # is the number at index equal to the number at num[i] ?
            # lets say i = 3, num[i] = 5. is num[num[i]] which is num[5] == 5?
            if tmp == nums[i]: # if yes
                nums[i] = -1 # make num[5] irrelevant
            else: # if no
                nums[nums[i]] = nums[i] # make num[5] = 5 
                nums[i] = tmp # num[3] = x ?
        # print(nums)        

    i = 1 # start from index 1
    while(i<=length): 
        if nums[i] != i: # now check if the number matches its index
            return i # when it doesnt, return index
        i = i +1
    return i # return 1 or the last


def main():

    arr = [39,8,43,12,38,11,-9,12,34,20,44,32,10,22,38,9,45,26,-4,2,1,3,3,20,38,17,20,25,41,35,37,18,37,34,24,29,39,9,36,28,23,18,-2,28,34,30]
    
    missing = firstMissingPositive(arr)
    
    print(missing)

if __name__ == "__main__":
    main()