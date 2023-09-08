class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """

        res = ''

        # indexstrs = 0
        # indexword = 0


        for i, n in enumerate(strs[0]):
            for word in strs:
                if len(word) > i:
                    if word[i] != n:
                        return res
                else:
                    return res
            res += n
        return res



        
print(Solution().longestCommonPrefix(["dog","racecar","car"]))