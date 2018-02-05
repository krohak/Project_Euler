def partition(arr,p,r):
    v = arr[p]
    i = p+1
    j = r-1

    while(True):

        while (arr[i] < v):
            i+=1
        while (arr[j] > v):
            j-=1

        if(i<j):
            arr[i], arr[j] = arr[j], arr[i]
            print(arr, i, j)
        elif(j>i):
            return j



def quick_sort(arr,p,r):
    if (r>p):
        q = partition(arr,p,r)
        quick_sort(arr,p,q)
        quick_sort(arr,q+1,r)
    else:
        return arr


random_list = [7,432,9,2,5,2,3245]
print(quick_sort(random_list,0,len(random_list)))

'''import numpy as np
for k in range(100):
    n=100
    random_list = np.random.rand(100)*100

    #print(random_list)
    #bubble_sort(random_list,n)
    #insertion_sort(random_list,n)
    random_list = quick_sort(random_list,0,n)
    print(all(random_list[i] <= random_list[i+1] for i in range(len(random_list)-1)))'''
