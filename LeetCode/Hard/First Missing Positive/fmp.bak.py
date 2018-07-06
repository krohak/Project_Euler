


def firstMissingPositive(nums):

    if len(nums) <= 1:
        return 1

    if len(nums) == 2:
        if nums[0] > 0 and nums[0]*nums[1] == 2:
            return 3
        else:
            return 1

    pointer = nums.pop(0)
    least = pointer

    for elem in nums:
        if elem < least:
            least = elem

        if elem == pointer+1:
            pointer = elem
        elif elem < pointer and not pointer - elem == 1 and not elem == least:
            pointer = elem


    
    print(least, pointer)

    if least > 1:
        return 1

    if pointer <= 0:
        return 1

    return pointer+1 



def main():
    # arr = [2,0,1]

    # arr = [1,2,0]

    # arr = [7,8,9,11,12]

    arr = [1000,-1]

    print(firstMissingPositive(arr))

if __name__ == "__main__":
    main()