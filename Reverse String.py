class Solution(object):
    def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        l = 0
        r = len(s) - 1

        while r > l:
            s[l], s[r] = s[r], s[l]
            r -= 1
            l += 1
        