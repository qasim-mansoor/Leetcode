class Solution(object):
    def combinationSum4(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        dp = {}
        dp[0] = 0

        val = 1

        while val <= target:
            dp[val] = 0

            for num in nums:
                if val - num >= 0:
                    if val - num == 0:
                        dp[val] += 1
                    dp[val] += dp[val-num]


            # print(dp)  



            val += 1
        return dp[target]
        # d[1] = 1
        # d[2] = 1 + 1
        # d[3] = 2 + 1 + 1
        # d[4] = 4 + 2 + 1