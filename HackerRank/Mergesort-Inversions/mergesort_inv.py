#!/bin/python3

import sys

def merge_sort(arr,inversion_count):

    # if len <= 1, return
    if len(arr) <= 1:
        return arr, 0

    # split the array in equal halves
    n = len(arr)
    arr1 = arr[0:n//2]
    arr2 = arr[n//2:]


    # call mergesort on halves
    arr1, inversion_count1 = merge_sort(arr1,inversion_count)
    arr2, inversion_count2 = merge_sort(arr2,inversion_count)

    # combine halves
    inversion_count = inversion_count1 + inversion_count2

    count1 = 0
    count2 = 0
    i = 0

    while(i < len(arr) and count1 < len(arr1) and count2 < len(arr2)):
        if (arr1[count1] <= arr2[count2]):
            arr[i] = arr1[count1]
            count1+=1
            i+=1

        else:
            arr[i] = arr2[count2]
            count2+=1
            i+=1
            inversion_count+=count2

    while (count1 < len(arr1)):
        arr[i] = arr1[count1]
        count1+=1
        i+=1
        inversion_count+=count2

    while (count2 < len(arr2)):
        arr[i] = arr2[count2]
        count2+=1
        i+=1


    return arr,inversion_count


def count_inversions(arr):
    arr,inversion_count = merge_sort(arr,0)
    return inversion_count


if __name__ == "__main__":
    t = int(input().strip())
    for a0 in range(t):
        n = int(input().strip())
        arr = list(map(int, input().strip().split(' ')))
        result = count_inversions(arr)
        print(result)
