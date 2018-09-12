class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        # nums1 is the smaller array
        n, m = len(nums1), len(nums2)
        if m < n:
            nums1, nums2, n, m = nums2, nums1, m, n

        i, j =  0, 0
        min_index, max_index = 0, n

        while(min_index<=max_index):

            i = (min_index+max_index)//2 # take something from nums1
            j = (n+m+1)//2 - i # take lesser from nums2 if more from nums1 and vice versa
            # the "+1" in the above line ensures that number of elements
            # in first half is always >= num elements in second half

            if i<n and nums1[i] < nums2[j-1]:
                min_index = i+1 # take more from nums1

            elif i>0 and nums2[j] < nums1[i-1]:
                max_index = i-1 # take less from nums1

            # parfectly parititioned both nums
            else: 
                break


        med_low, med_high = 0, 0
        
        # handle nums1[:i] empty 
        if i==0:
            med_low = nums2[j-1]
        # handle nums2[:j] empty
        elif j==0:
            med_low = nums1[i-1]
        else:
            med_low = max(nums1[i-1],nums2[j-1])
        
        # if odd num of elements in total
        if (n+m)%2 == 1:
            return med_low

        # even 
        # handle nums1[i:] empty
        if i==n:
            med_high = nums2[j]
        # handle nums2[j:] empty 
        elif j==m:
            med_high = nums1[i]
        else:
            med_high = min(nums1[i],nums2[j])
        return (med_low+med_high) / 2
        