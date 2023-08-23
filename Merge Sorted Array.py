class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        nums3 = []
        i1 = 0
        i2 = 0
        for i in range(m+n):
            if(nums1[i1] > nums2[i2]):
                nums3.append(nums2[i2])
                i2+=1
            elif(nums1[i1] == 0 and i2 == n):
                break
            elif(nums1[i1] == 0):
                nums3.append(nums2[i2])
                i2+=1
            else:
                nums3.append(nums1[i1])
                i1+=1
        
        nums1 = nums3
        print(nums1)

x = Solution()
nums1 = [1]
m = 1
nums2 = []
n = len(nums2)
x.merge(nums1, m, nums2, n)