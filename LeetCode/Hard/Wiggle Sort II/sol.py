def Partition(arr, low, high):
    
    ref = arr[high]
    i = low
    j = low
    while j < high:

        if arr[j] < ref:
            arr[j], arr[i] = arr[i], arr[j]
            i+=1

        j+=1

    part = i
    while(arr[i] == ref and i<high):
        i+=1

    arr[i], arr[high] = arr[high], arr[i]
    return part


def QuickSelect(arr, k ,low, high):

    med = Partition(arr, low, high)

    if med == k:
        return k

    elif med < k:
        return QuickSelect(arr, k, med+1, high)

    elif med > k:
        return QuickSelect(arr, k, low, med-1)


def WiggleSort(arr, part, n):

    # find index of first instance of median
    med_first = 0
    while med_first<n and arr[med_first]!=arr[part]:
        med_first+=1

    if med_first%2!=0:
        med_first+=1

    # handle < median at odd position from start
    i = 1
    fill = med_first
    while i<part and fill<n:

        if arr[i]<arr[part]:
            arr[i], arr[fill] = arr[fill], arr[i]
            fill+=2
        i+=2

    print(arr, 'less than median pass')

    # find last index of <median
    med_last = n-1
    while med_last>=0 and arr[med_last]>arr[part]:
        med_last-=1

    if med_first%2!=1:
        med_first-=1

    # handle > median at even position from end
    if (n-1)%2 == 0:
        i = n-1
    else:
        i = n-2

    fill = med_last
    
    while i>med_last and fill>0:
        if arr[i]>arr[part]:
            arr[i], arr[fill] = arr[fill], arr[i]
            fill-=2
        i-=2

    return arr




list1 = [5,4,5,4,5,6,6,6,5]
# list1 = [0,1,2,3,4]
print(list1, 'original')
n = len(list1)
med = QuickSelect(list1, n//2, 0, n-1)
# print(med)
print(list1, 'partitioned')

arr = WiggleSort(list1, med, n)
print(arr)