# divide the array into pos and neg+0, return pos
def dividePositive(nums):
    forward = 0 # looks for negative and zero in front
    backward = len(nums)-1 # looks for positive at back
    while forward <= backward: 
        while nums[backward] <= 0 and not backward < 0:
            backward -= 1
        while nums[forward] > 0 and not forward >= len(nums)-1 :
            forward += 1
        if forward <= backward:
            nums[forward], nums[backward] = nums[backward], nums[forward]
            backward -= 1
            forward += 1 
    # print(nums, forward, backward)
    return nums[:forward]

def firstPositive(nums):
    pointer = nums[0]
    for elem in nums:
        if elem < pointer and elem>0:
            pointer = elem
    return pointer

def findGreatest(nums):
    pointer = nums[0]
    for elem in nums:
        if elem > pointer:
            pointer = elem
    return pointer

# divide array based on a given number 'middle'
def divideArray(nums, middle, first, last):

    forward = first # looks for greater than middle at back
    backward = last-1 # looks for less then equal to middle

    while forward <= backward: 
        while nums[backward] > middle and not backward < 0:
            backward -= 1

        while nums[forward] <= middle and not forward == len(nums)-1 :
            forward += 1
        
        if forward <= backward:
            nums[forward], nums[backward] = nums[backward], nums[forward]
            backward -= 1
            forward += 1    
    # print("Pointers %s, %s"%(forward, backward))
    return nums, forward

def missingInPositiveSequence(nums):
    # find middle index of nums acc to len(nums)
    # move x > middle index to right and x < to left
    # if x at mid is middle, middleFind[middleindex:]
    # if x at mid > middle index, middleFind[:middleindex]
    # when len(nums) == 1, return number

    first = 0
    last  = len(nums)
    middle = (last+first) // 2
    # print(first, middle, last)

    while first <= last and last <= len(nums) and middle < last and middle > first:

        # print("Before divide array:")
        # print(nums)
        prev_first = first
        prev_last = last

        print("Initial: first: %s, middle: %s, last: %s"%(first,middle,last))
        nums, pointer = divideArray(nums, middle, first, last)
        # print(pointer)
        # print("After divide array: ")
        # print(nums)
        if pointer == len(nums):
            break

        # if there are exactly the same amount of
        # numbers in left half as the index of mid 
        # [ie, there are no missing numbers in the sequence till now ]
        if len(nums[:pointer]) == middle:                                  
            # missing num must exist in right half
            # print("here")
            first = pointer

        else:
            # missing number lies in left half
            last = pointer+1

        middle = (last+first) // 2

        if prev_first == first and prev_last == last:
            break
   
    missing = middle+1
    return missing

def removeDuplicates(nums):
    uniq = set()
    for elem in nums:
        uniq.add(elem)
    
    nums_uniq = []
    for elem in uniq:
        nums_uniq.append(elem)
    
    return nums_uniq

def firstMissingPositive(nums):

    if len(nums) == 0:
        return 1
    if len(nums) == 1:
        if nums[0] == 1:
            return 2
        else:
            return 1
    
    nums = removeDuplicates(nums)
    nums = dividePositive(nums) # filter out the negatives
    greatest = findGreatest(nums)
    first_positive = firstPositive(nums)

    if first_positive > 1:
        # seq begins from a number > 1, 
        # hence 1 is first missing positive
        return 1
    
    if greatest == first_positive:
        return first_positive+1

    if first_positive <= 1:
        missing = missingInPositiveSequence(nums)

        if missing == greatest:
            return missing+1
        else:
            return missing

def main():
    # arr = [2,0,1]
    # arr = [1,2,0]
    # arr = [7,8,9,11,12]
    # arr = [4,1,2,3]
    # arr = [3,4,-1,1]
    # # print(firstMissingPositive(arr))

    # arr = [4,-7,-8,-134,2,1,-3,5]
    # arr = divideArray(-1,arr)
    # print(arr)

    # arr = [1,2,3,4,5,6,7,8,9,11]
    # arr = [1, 2, 3, 4, 5, 6, 7, 11, 9]
    # arr = [9,1,5,20,8,3,6,101,4]
    # arr = [1,2,3,4,5,6,7,101,-3]
    # arr = [0,2,2,1,1]
    # arr = [1,1,1,1,1,3]
    arr = [39,8,43,12,38,11,-9,12,34,20,44,32,10,22,38,9,45,26,-4,2,1,3,3,20,38,17,20,25,41,35,37,18,37,34,24,29,39,9,36,28,23,18,-2,28,34,30]
    missing = firstMissingPositive(arr)
    print(missing)

if __name__ == "__main__":
    main()