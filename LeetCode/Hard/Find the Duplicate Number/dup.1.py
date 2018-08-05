def isCycle(arr, i, size):
    ref = i
    j = arr[ref-1]
    elem_count = 1

    while j != ref and elem_count < size:
        j = arr[j-1]
        elem_count+=1
    
    if elem_count>=size:
        return 0
    
    else:
        return 1

def duplicateInCycle(arr, i , size):
    duplicate = arr[i-1]

    while not isCycle(arr, i , size):
        duplicate = arr[i-1]
        i = arr[i-1]
    
    return duplicate
    

class Solution:
    def findDuplicate(self, arr):

        size = len(arr)+1
        i = 1

        while i<size:
            cycle_bool = isCycle(arr, i, size)

            if cycle_bool:
                i+=1
            else:
                return duplicateInCycle(arr, i , size)

arr = [1,3,4,2,2]
arr = [3,1,3,4,2]
dup = Solution().findDuplicate(arr)
print(dup)