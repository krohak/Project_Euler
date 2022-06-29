class Solution:
    def merge(self, nums1, m, nums2, n):
        """
        Do not return anything, modify nums1 in-place instead.
        """
        
        nums1_pointer = m-1
        nums2_pointer = n-1
        
        pointer = len(nums1)-1
        
        while pointer >= 0:
            
            if nums2_pointer < 0:
                nums1[pointer] = nums1[nums1_pointer]
                nums1_pointer-=1
            
            elif nums1_pointer < 0:
                nums1[pointer] = nums2[nums2_pointer]
                nums2_pointer-=1
            
            elif nums1[nums1_pointer] >= nums2[nums2_pointer]:
                nums1[pointer] = nums1[nums1_pointer]
                nums1_pointer-=1
            
            else:
                nums1[pointer] = nums2[nums2_pointer]
                nums2_pointer-=1
            
            pointer-=1
            
        return
                