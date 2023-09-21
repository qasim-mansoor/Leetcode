class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dp = {}

        i = len(nums) - 1
        dp[i] = nums[i]
        dp[i + 1] = 0
        dp[i + 2] = 0
        i -= 1

        while i >= 0:
            dp[i] = max(nums[i] + dp[i + 2], nums[i] + dp[i + 3], dp[i+1])
            i -= 1

        return dp[0]
            
