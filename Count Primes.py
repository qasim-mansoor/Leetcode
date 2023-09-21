class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        if  n <= 2:
            return 0

        comp = [False] * n

        limit = int(n ** 0.5) 

        for i in range(2, int(n ** 0.5) + 1):
            if(comp[i] == False):
                for j in range(i*i, n, i):
                    comp[j] = True

        count = 0
        for i in range(2, n):
            if not comp[i]:
                count += 1

        return count


        