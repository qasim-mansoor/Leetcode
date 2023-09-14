class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        for i in range(len(nums)):
            if abs(nums[i]) < len(nums):
                nums[abs(nums[i])] = nums[abs(nums[i])] * -1
            
                if (nums[abs(nums[i])] == 0):
                    nums[abs(nums[i])] = len(nums) + 1
            
            if abs(nums[i]) > len(nums):
                nums[0] = nums[0] * -1

        for i in range(len(nums)):
            if(0 <= nums[i] <  len(nums) + 1):
                return i

        return len(nums)
        