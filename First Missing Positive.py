class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        present = [False] * (len(nums)+2)
        print(present)

        for i in range(len(nums)):
            if(nums[i] > 0 and nums[i] < len(nums)+1):
                present[nums[i]] = True
        print(present)

        for i in range(1, len(present)):
            if not present[i]:
                return i 
        

print(Solution().firstMissingPositive([1,2,4,5,6,7]))