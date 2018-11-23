# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

import math


def calBinarian(list1):

    sum_list = 0
    for elem in list1:
        sum_list+= 2**elem

    return sum_list


def minBinarian(number):

    if number == 0:
        return 1

    L = [0 for num in range(number+1)]
    # print(L)

    for x in range(1,number+1):

        power = math.log(x,2)
        if power.is_integer():
            L[x] = 1
        
        else:
            min_branch = float('Inf')
            for y in range(int(power)):
                min_branch = min(min_branch, L[x - 2**y])

            L[x] = min_branch+1

    # print(L)
    return L[number]

def solution(A):
    # write your code in Python 3.6
    binarian = calBinarian(A)
    return minBinarian(binarian)


A = [2,2,1]
sol = solution(A)
print(sol)