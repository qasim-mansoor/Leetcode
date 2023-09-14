class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        vals = {}

        for char in s:
            if char in vals:
                vals[char] += 1
            else:
                vals[char] = 1

        for char in t:
            if char in vals:
                vals[char] -= 1
                if vals[char] == 0:
                    del vals[char]
            else:
                return False
            
        if vals:
            return False
        else:
            return True
        