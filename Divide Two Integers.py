class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        
        n = abs(dividend)
        d = abs(divisor)
        count = 0
        if(abs(divisor) == 1):
            count = abs(dividend)
        else:
            while(n >= d):
                n = n - d
                count += 1

        if((dividend > 0 and divisor > 0) or (dividend < 0 and divisor < 0)):
            return count
        else:
            return (count) - (count) - (count)
        
print(Solution().divide(1,1))

        
