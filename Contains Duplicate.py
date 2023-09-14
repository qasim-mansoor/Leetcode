class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """

        vals = {}

        for num in nums:
            if num in vals:
                return True
            else:
                vals[num] = 1
        
        return False
        