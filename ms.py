#!/bin/python3

import sys
from copy import deepcopy

def MergeSort(arr):
    length = len(arr)
    if length == 1:
        return
    l1=length//2
    l2=length-l1
    A = arr[:l1]
    B = arr[l1:]
    print(A,B)

    MergeSort(A)
    MergeSort(B)

    countA,countB=0,0

    for i in range(length):
        if countA<l1 and (countB>=l2 or A[countA]<=B[countB]):
            arr[countA]=A[countA]
            countA+=1

        elif countB<l2:
            arr[countB]=B[countB]
            countB+=1

    print(arr)


def countInversions(arr):

    C=deepcopy(arr)
    MergeSort(C)

    print(C)
    count=0

    for i,j in zip(C,arr):
        if not i==j:
            count+=1

    return count


for _ in range(input()):
    n = input()
    arr = map(int,raw_input().split())
    print(arr)
    countInversions(arr)
    print arr






'''
while (countA<l1 and countB<l2):
        if (A[countA]<=B[countB]):
            arr[i]=A[countA]
            countA+=1
            i+=1

        else:
            arr[i]=B[countB]
            countB+=1
            i=+1

    while countA<l1:
        print(i)
        arr[i]=A[countA]
        countA+=1
        i+=1

    while countB<l2:
        print(i)
        arr[i]=B[countB]
        countB+=1
        i+=1
'''
