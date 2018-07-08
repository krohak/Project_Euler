
def dividePositive(nums):

    forward = 0 # looks for negative and zero in front
    backward = len(nums)-1 # looks for positive at back

    while forward <= backward: 
        while nums[backward] <= 0 and not backward < 0:
            backward -= 1

        while nums[forward] > 0 and not forward >= len(nums) :
            forward += 1
        
        if forward <= backward:
            nums[forward], nums[backward] = nums[backward], nums[forward]
            backward -= 1
            forward += 1    
        
    print(nums, forward, backward)
    return nums[:forward]

def firstPositive(nums):
    pointer = nums[0]

    for elem in nums:
        if elem < pointer and elem>0:
            pointer = elem

    return pointer

def firstMissingPositive(nums):

    pointer = firstPositive(nums)

    if pointer > 1:
        return 1

    if pointer <= 1:
        # do something
        # middleFind()
        for elem in nums:
            if elem == pointer+1:
                pointer = elem
        
        return pointer+1

def middleFind(nums):
    # find middle index of nums acc to len(nums)
    # move x > middle index to right and x < to left
    # if x at mid is middle, middleFind[middleindex:]
    # if x at mid > middle index, middleFind[:middleindex]
    # when len(nums) == 1, return number
    pass

def main():
    # arr = [2,0,1]
    # arr = [1,2,0]
    # arr = [7,8,9,11,12]
    # arr = [4,1,2,3]
    # arr = [3,4,-1,1]
    # print(firstMissingPositive(arr))

    arr = [4,-7,-8,134,2,1,-3,5]
    arr = dividePositive(arr)
    print(arr)

if __name__ == "__main__":
    main()