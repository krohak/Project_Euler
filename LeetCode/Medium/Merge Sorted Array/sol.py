class Solution(object):
    def merge(self, nums1, m, nums2, n):
        read1, read2 = m-1, n-1
        write = m+n-1
        while(write >= 0):
            if read2 < 0 or (read1>=0 and nums1[read1] >= nums2[read2]):
                nums1[write] = nums1[read1]
                read1-=1
            else:
                nums1[write] = nums2[read2]
                read2-=1
            write-=1
        return nums1