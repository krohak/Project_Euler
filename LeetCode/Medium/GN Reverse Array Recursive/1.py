from copy import deepcopy

arr = [1,2,3,4]
n = len(arr)

# [1,2,3,4]
# [1,2]
# [2,1]
# [3,4]
# [4,3]
# [4,3,2,1]
# [1,2,3,4,5,6,7,8]

# [8,7,6,5]
# [4,3,2,1]
# [8,7,6,5,4,3,2,1]


# [1,2,3,4]

# 4 3 2 1


# 2,3,4,5

# 1,2,3,4,5,6
# 6,5,4,3,2,1


# 1,2,4,5 [6]
# 5,4,2,1


# 6,5,4,2,1



def recursiveReverse(arr):
    if len(arr)<2: return arr
    return [arr[-1]] + recursiveReverse(arr[:-1])



arr = [1,2,3,4,5,6,7,8]
# arr = [1,2,3,4,5]
# arr = []
print(recursiveReverse(arr))

def realRecursive(arr):
    if len(arr)<=1:
        return arr
    leftHalf, rightHalf = deepcopy(arr[:len(arr)//2]), deepcopy(arr[len(arr)//2:])
    reversedLeft = realRecursive(leftHalf)
    reversedRight = realRecursive(rightHalf)
    return reversedRight+reversedLeft

# nlogn
# nlogn


def realRecursiveReverse(arr):
    if len(arr) == 1:
        return arr
    leftHalf, rightHalf = deepcopy(arr[:len(arr)//2]), deepcopy(arr[len(arr)//2:])
    leftMost, rightMost = leftHalf[0], rightHalf[-1]
    reversedLeft = realRecursiveReverse(leftHalf[1:])
    reversedRight = realRecursiveReverse(rightHalf[:-1])
    reversedLeft = [rightMost]+reversedLeft
    reversedRight = reversedRight + [leftMost]
    return reversedLeft+reversedRight

# print(realRecursiveReverse(arr))


def reverseArrInPlace(arr):
    first, last = 0, len(arr)-1
    while first < len(arr) // 2:
        arr[first], arr[last] = arr[last], arr[first]
        first+=1; last-=1
    return arr

def recursiveReversem(offset):
    if offset > n//2:
        return
    global arr
    arr[0+offset], arr[n-1-offset] = arr[n-1-offset], arr[0+offset]
    recursiveReverse(offset+1)


# arr = [1,2,3,4,5]
# print(reverseArrInPlace(arr))

# arr = [1,2,3,4]
# print(reverseArrInPlace(arr))

# arr = []
# print(reverseArrInPlace(arr))

# arr = [0,0,0,1]
# print(reverseArrInPlace(arr))