class Solution(object):
    def myAtoi(self, s):
        """
        :type s: str
        :rtype: int
        """
        num = 0
        multiplier = 1
        for i in range(len(s)):
            if(s[-(i+1)] != '+' and s[-(i+1)] != '-'):
                num = num + int(s[-(i+1)])*multiplier
                multiplier *= 10

        if(s[0] == '-'):
            num = num * - 1
        
        return num

print(Solution().myAtoi("-0042"))