def merge_sort(arr):

    # if len <= 1, return
    if len(arr) <= 1:
        return arr

    # split the array in equal halves
    n = len(arr)
    arr1 = arr[0:n//2]
    arr2 = arr[n//2:]


    # call mergesort on halves
    arr1 = merge_sort(arr1)
    arr2 = merge_sort(arr2)

    # combine halves
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

    while (count1 < len(arr1)):
        arr[i] = arr1[count1]
        count1+=1
        i+=1

    while (count2 < len(arr2)):
        arr[i] = arr2[count2]
        count2+=1
        i+=1

    return arr

#a = merge_sort([2,6,1,9,0,4,7,3,45])
#print(a)

import numpy as np
for k in range(100):
    n=100
    random_list = np.random.rand(100)*100

    #print(random_list)
    #bubble_sort(random_list,n)
    #insertion_sort(random_list,n)
    random_list = merge_sort(random_list)
    print(all(random_list[i] <= random_list[i+1] for i in range(len(random_list)-1)))
