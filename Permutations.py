class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []

        def rec(patt, rem):
            if not rem:
                res.append(patt)
                return

            for i, n in enumerate(rem):
                rec(patt + [n], rem[0:i] + rem[i+1:])


        rec([], nums)
        return res
