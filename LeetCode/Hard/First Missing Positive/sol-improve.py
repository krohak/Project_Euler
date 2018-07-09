def firstMissingPositive(nums):
    
    size = len(nums)
    i = 0
    nums.append(-1)

    while (i<size):
        # if num at correct index, negative or greater then size of array
        if nums[i] == i or nums[i] < 0 or nums[i] > size: 
            i+=1
        else:
            if nums[nums[i]] == nums[i]: # nums[nums[3]] == nums[5] ?
                nums[i] = -1 # mark
            else:
                tmp = nums[nums[i]] # nums[5] is x
                nums[nums[i]] = nums[i] # nums[5] = nums[3]
                nums[i] = tmp # nums[3] = x

    i = 1
    while (i<=size):
        if nums[i] != i:
            return i
        i+=1
    return i

def main():

    arr = [39,8,43,12,38,11,-9,12,34,20,44,32,10,22,38,9,45,26,-4,2,1,3,3,20,38,17,20,25,41,35,37,18,37,34,24,29,39,9,36,28,23,18,-2,28,34,30]
    missing = firstMissingPositive(arr)
    print(missing)

if __name__ == "__main__":
    main()