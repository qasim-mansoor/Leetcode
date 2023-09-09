class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        def MergeSort(nums):
            if not nums:
                return None
            else:
                if len(nums) == 1:
                    return nums
                
            m = (len(nums) - 1) // 2

            # print(nums, l, r, m)

            la = MergeSort(nums[:m+1])
            ra = MergeSort(nums[m+1:])
            res = []

            while la and ra:
                if la[0] < ra[0]:
                    res.append(la[0])
                    la.pop(0)
                else:
                    res.append(ra[0])
                    ra.pop(0)

            if ra:
                res.extend(ra)

            if la:
                res.extend(la)

            return res
        
        nums = MergeSort(nums)
        
        for i in range(0 , len(nums), 2):
            if i+1 >= len(nums):
                return nums[i]
            elif nums[i] != nums[i+1]:
                return nums[i]