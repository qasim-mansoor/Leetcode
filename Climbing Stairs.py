class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp = {}

        dp[1] = 1
        dp[2] = 2

        for i in range(3, n + 1):
            dp[i] = dp[i - 2] + dp[i - 1]

        return dp[n]


        # For 1:
        # 1

        # For 2:
        # 1 + 1
        # 2

        # For 3:
        # 1 + 1 + 1
        # 1 + 2
        # 2 + 1

        # For 4:
        # 1,1,1,1
        # 1,1,2
        # 1,2,1
        # 2,1,1
        # 2,2

        # For 5:
        # 1,1,1,1,1
        # 1,1,1,2
        # 1,1,2,1
        # 1,2,1,1
        # 2,1,1,1
        # 2,2,1
        # 1,2,2
        # 2,1,2  
