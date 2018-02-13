#!/bin/python3
import sys
from copy import deepcopy

def merge_sort(arr,inversion_count):

    # if len <= 1, return
    if len(arr) <= 1:
        return arr, 0

    # split the array in equal halves
    n = len(arr)
    arr1 = deepcopy(arr[0:n//2])
    arr2 = deepcopy(arr[n//2:])


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
            if (arr1[count1] > 2*arr2[count2-1] and count2 != 0):
                inversion_count+=count2
            arr[i] = arr1[count1]
            count1+=1
            i+=1


        else:
            arr[i] = arr2[count2]
            count2+=1
            i+=1


    while (count1 < len(arr1)):
        if (arr1[count1] > 2*arr2[count2-1] and count2 != 0):
            print(arr1[count1],arr2[count2-1])
            inversion_count+=count2
        arr[i] = arr1[count1]
        count1+=1
        i+=1


    while (count2 < len(arr2)):
        arr[i] = arr2[count2]
        count2+=1
        i+=1


    return arr,inversion_count


def count_inversions(arr):
    print(arr)
    arr,inversion_count = merge_sort(arr,0)
    print(arr)
    return inversion_count


import numpy as np

#n=100
#random_list = np.random.rand(5)*100
#print(random_list)
random_list = [1,88,86,194,53]
c = count_inversions(random_list)
print(c)
