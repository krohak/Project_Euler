def shiftArrayByNegativeMin(arr):
    min_num = min(arr)
    if min_num < 0:
        for i in range(len(arr)):
            arr[i] += abs(min_num)
    return arr

def initializeBuckets(bucket_set):
    bucket_set = []
    for _ in range(10):
        bucket_set.append([])
    return bucket_set

def flattenBuckets(bucket_set):
    arr = []
    for bucket in bucket_set:
        for num_str in bucket:
            arr.append(num_str)
    return arr

def intArrToStringArr(arr):
    m = len([c for c in str(max(arr))])
    for i, num in enumerate(arr):
        num_str = str(num)
        num_len = len([c for c in num_str])
        for _ in range (m-num_len):
            num_str = '0'+num_str
        arr[i] = num_str
    return arr

def radixSort(arr):
    arr = intArrToStringArr(arr)
    bucket_set = []
    bucket_set = initializeBuckets(bucket_set)

    max_num = max(arr)
    m = len([c for c in str(max_num)])

    for i in reversed(range(m)):
        for num_str in arr:
            bucket_index = int(num_str[i])
            bucket_set[bucket_index].append(num_str)
        arr = flattenBuckets(bucket_set)
        bucket_set = initializeBuckets(bucket_set)
    arr = [int(num) for num in arr]
    return arr

class Solution:
    def longestConsecutive(self, arr):

        arr_set = set(arr)
        arr = list(arr_set)
        
        if len(arr) == 0:
            return 0
        elif len(arr) == 1:
            return 1
        
        arr = shiftArrayByNegativeMin(arr)
        print(arr)
        arr = radixSort(arr)
        print(arr)

        i = 0 
        max_conseq = 0
        while i < len(arr)-1:
            conseq = 1
            while i < len(arr)-1:
                if arr[i] + 1 == arr[i+1]:
                    conseq+=1
                    i+=1
                else:
                    break
            if conseq > max_conseq:
                max_conseq = conseq
            i+=1
        return max_conseq


# arr = [100,4,200,1,3,2]
arr = [0,-1]
# arr = [1,2,3,4]

# arr = [9,1,4,7,3,-1,0,5,8,-1,6]

solobj = Solution()
max_conseq = solobj.longestConsecutive(arr)
print(max_conseq)
