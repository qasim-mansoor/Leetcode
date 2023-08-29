class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        maxlen = 0
        localsum = 0
        vals = {}
        for char in s:
            
            if char not in vals:
                vals[char] = 1

                localsum += 1
            else:

                maxlen = max(localsum, maxlen)
                localsum = 1
                vals = {}
                vals[char] = 1
            
        return maxlen

        

print(Solution().lengthOfLongestSubstring("pwwkew"))