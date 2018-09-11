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
        return k

    elif med < k:
        return QuickSelect(arr, k, med+1, high)

    elif med > k:
        return QuickSelect(arr, k, low, med-1)


def WiggleSort(arr, n, med):

    result = []

    left = 0
    right = med

    alternate = 0
    while (not alternate and left<med) or (alternate and right<n):

        if not alternate:
            result.append(arr[left])
            left+=1
            alternate=1-alternate
        else:
            result.append(arr[right])
            right+=1
            alternate=1-alternate
    
    if right<n:
        if arr[right+1] > arr[right]:
            result.append(arr[right+1])
        else:
            result.append(arr[right])

    return result


def WiggleSortInPlace(arr, n, med):
    pass

arr = [1, 5, 1, 1, 6, 4]
print(arr)
n = len(arr)
med = QuickSelect(arr, n//2, 0, n-1)
print(med)
print(arr)

result = WiggleSort(arr, n, med)
print(result)