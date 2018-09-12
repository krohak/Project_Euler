def Partition(arr, low, high):
    
    ref = arr[high]
    i = low
    j = low
    while j < high:

        if arr[j] < ref:
            arr[j], arr[i] = arr[i], arr[j]
            i+=1

        j+=1

    arr[i], arr[high] = arr[high], arr[i]
    return i


def QuickSelect(arr, k ,low, high):

    med = Partition(arr, low, high)

    if med == k:
        return arr[k]

    elif med < k:
        return QuickSelect(arr, k, med+1, high)

    elif med > k:
        return QuickSelect(arr, k, low, med-1)


list1 = [4,10,1,11,5,9,17]
print(list1)
n = len(list1)
med = QuickSelect(list1, n//2, 0, n-1)
print(med)
print(list1)