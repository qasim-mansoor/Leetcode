class Solution(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp = {}
        dp[0] = 0
        dp[1] = 1
        for i in range(2, n+1):
            minsteps = n
            for j in range(int(i**0.5), 0, -1):
                minsteps = min(minsteps,dp[i-(j*j)] + 1)
            dp[i] = minsteps
        
        return dp[n]
