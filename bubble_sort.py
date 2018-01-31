import numpy as np

# bubble up elements which are greatest
# only swaps allowed
def bubble_sort(a,n):
    for i in range(n):
        for j in range(n-i-1):
            if (a[j]>a[j+1]):
                a[j],a[j+1] = a[j+1], a[j]
    return a

# insert in list which is being maintained starting from a[0]
# only swaps allowed
def insertion_sort(a,n):
    for i in range(1,n):
        for j in reversed(range(0,i)):
            if a[j+1] < a[j]:
                a[j+1],a[j] = a[j], a[j+1]

    return a


# pickup greatest element, put at the end of the list
def selection_sort(a,n):
    for i in reversed(range(1,n)):
        max_j = 0
        for j in range(0,i+1):
            if a[j]>a[max_j]:
                max_j=j
        a[i], a[max_j] = a[max_j], a[i]

    return a


for k in range(100):
    n=100
    random_list = np.random.rand(100)*100

    #print(random_list)
    #bubble_sort(random_list,n)
    #insertion_sort(random_list,n)
    selection_sort(random_list,n)
    print(all(random_list[i] <= random_list[i+1] for i in range(len(random_list)-1)))
