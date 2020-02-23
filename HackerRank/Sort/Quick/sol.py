
def call_quick_sort(arr):
    n = len(arr)
    quick_sort(arr, 0, n-1, n)
    return arr

def quick_sort(arr, start, end, n):

    if start>=end:
        return

    index = pick_pivot_and_place(arr, start, end)
    if index>0:
        quick_sort(arr, start, index-1, n)
    if index<n-1:
        quick_sort(arr, index+1, end, n)


def pick_pivot_and_place(arr, start, end):

    pivot_elem = arr[start]
    left = start+1
    right = end

    while(left<right):

        while(left<right and arr[left]< pivot_elem):
            left+=1
        while(left<right and arr[right]>pivot_elem):
            right-=1
        
        if left<right:
            arr[left], arr[right] = arr[right], arr[left]
            left+=1
            right-=1

    arr[right], arr[start] = arr[start], arr[right]
    return right

arr = [3,6,10,2,7,4,5,9,1,8]
# arr =  [1,1,1,0,0,0,0]
# arr = [3,6,10,2,7,4,5,9,1,8,3,6,10,2,7,4,5,9,1,8]
ans = call_quick_sort(arr)
print(ans)