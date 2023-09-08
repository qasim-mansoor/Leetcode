class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        print(nums1, nums2)
        while nums1[0] != 0:
            if nums1[0] < nums2[0]:
                nums1.append(nums1.pop(0))
            else: 
                nums1.append(nums2.pop(0))

        while nums2:
            nums1.append(nums2.pop(0))
            
        while nums1[0] == 0:
            nums1.pop(0)
        
        print(nums1)

Solution().merge([1,2,3,0,0,0], 3, [2,5,6], 3)
