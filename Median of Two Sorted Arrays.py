class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        m = len(nums1)
        n = len(nums2)
        nums3 = []
        i1 = 0
        i2 = 0
        while(i1+i2!=m+n):
            if(i1 == m):
                nums3.append(nums2[i2])
                i2+=1
            
            elif(i2 == n):
                nums3.append(nums1[i1])
                i1+=1

            elif(nums1[i1] > nums2[i2]):
                nums3.append(nums2[i2])
                i2+=1

            elif(i2 != n):
                nums3.append(nums1[i1])
                i1+=1

        median = nums3[int(len(nums3)/2)] if len(nums3)/2 % 2 != 0 else (nums3[int(len(nums3)/2)]+nums3[int(len(nums3)/2)-1])/2
        return median

print(Solution().findMedianSortedArrays([1,2],[3,4]))