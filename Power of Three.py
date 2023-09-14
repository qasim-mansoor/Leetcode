class Solution(object):
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n == 1:
            return True

        while n >= 3:
            if n == 3:
                return True
            n = n / 9.0
            if n !=  int(n):
                return False
            print(n)
            
        if n == 1:
            return True
        return False