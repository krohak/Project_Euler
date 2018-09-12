def findMedianSortedArrays(nums1, nums2):
    # nums1 is the smaller array

    i, j =  0, 0
    med_low, med_high = 0, 0
    n, m = len(nums1), len(nums2)
    min_index, max_index = 0, n

    while(min_index<=max_index):

        i = int((min_index+max_index) / 2) # take something from nums1
        j = int(((n+m+1) / 2) - i) # take lesser from nums2 if more from nums1 and vice versa
        # the "+1" in the above line ensures that number of elements
        # in first half is always >= num elements in second half

        if i<n and j>0 and nums1[i] < nums2[j-1]:
            min_index = i+1 # take more from nums1

        elif i>0 and j<m and nums2[j] < nums1[i-1]:
            max_index = i-1 # take less from nums1

        # parfectly parititioned both nums
        else: 
            # handle nums1[:i] empty 
            if i==0:
                print(i, j, n, m)
                med_low = nums2[j-1]
                break
            # handle nums2[:j] empty
            elif j==0:
                print(i, j, n, m)
                med_low = nums1[i-1]
                break
            else:
                med_low = max(nums1[i-1],nums2[j-1])
                break

    # if odd num of elements in total
    if (n+m)%2 == 1:
        return med_low

    # even 
    else:
        # handle if nums1[i:] empty
        if i==n:
            print(i, j, n, m)
            med_high = nums2[j]
        # handle if nums2[j:] empty
        elif j==m:
            print(i, j, n, m)
            med_high = nums1[i]
        else:
            med_high = min(nums1[i],nums2[j])
        
        print(med_low, med_high)
        return (med_low+med_high) / 2
    


nums1 = [900]
nums2 = [10, 13, 14]

nums2 = [1,3]
nums1 = [2]


if (len(nums1) < len(nums2)) :
    print ("n< m; The median is : {}".format(findMedianSortedArrays(nums1, nums2)))
else :
    print ("The median is : {}".format(findMedianSortedArrays(nums2, nums1)))
 