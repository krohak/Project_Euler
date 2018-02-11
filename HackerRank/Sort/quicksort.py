def partition(arr,p,r):
    v = arr[r]
    i = p

    for j in range(p,r):
        if arr[j] <= v:
            arr[j], arr[i] = arr[i], arr[j]
            i+=1

    arr[i], arr[r] = arr[r], arr[i]
    return i

def quick_sort(arr,p,r):
    if (r>p):
        q = partition(arr,p,r)
        quick_sort(arr,p,q)
        quick_sort(arr,q+1,r)

        return arr


random_list = [7,432,9,5,2,3245]
print(quick_sort(random_list,0,len(random_list)-1))

'''import numpy as np
for k in range(100):
    n=100
    random_list = np.random.rand(100)*100

    #print(random_list)
    #bubble_sort(random_list,n)
    #insertion_sort(random_list,n)
    random_list = quick_sort(random_list,0,n)
    print(all(random_list[i] <= random_list[i+1] for i in range(len(random_list)-1)))'''
