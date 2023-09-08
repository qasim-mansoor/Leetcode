class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        uniq = 1
        last = nums[0]

        for i in range(1,len(nums)):
            if(nums[i] != last):
                last = nums[i]
                nums[uniq] = nums[i]
                uniq += 1

        
        return uniq
