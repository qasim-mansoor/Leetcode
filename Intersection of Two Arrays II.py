class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        vals = {}
        res = []

        for num in nums1:
            if num in vals:
                vals[num] += 1
            else:
                vals[num] = 1

        for num in nums2:
            if num in vals:
                vals[num] -= 1
                if vals[num] == 0:
                    del vals[num]
                res.append(num)

        return res 