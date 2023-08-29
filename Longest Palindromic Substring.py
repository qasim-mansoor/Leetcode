class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        res_l = 0
        res_r = 0
        reslen = 0

        for i in range(len(s)):
            if(len(s) % 2 == 1):
                l,r = i,i
                while l >= 0 and r < len(s) and s[l] == s[r]:
                    if(r-l+1) > reslen:
                        res_l = l
                        res_r = r
                        reslen = r-l+1
                    l-=1
                    r+=1

            else:
                l,r = i, i+1
                while l >= 0 and r < len(s) and s[l] == s[r]:
                    if(r-l+1) > reslen:
                        res_l = l
                        res_r = r
                        reslen = r-l+1
                    l-=1
                    r+=1
        return s[res_l:res_r+1]

print(Solution().longestPalindrome("racecar"))