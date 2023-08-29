class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        vals = {}
        
        for i, n in enumerate(nums):
            diff = target - n
            if diff in vals:
                return [vals[diff], i]
            vals[n] = i

print(Solution().twoSum([3,3], 6))