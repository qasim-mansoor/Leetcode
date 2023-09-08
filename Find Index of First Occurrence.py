class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """

        for i, char in enumerate(haystack):
            if char == needle[0]:
                if(haystack[i+1:len(needle)+i] == needle[1:len(needle)]):
                    return i
            
        return -1
        
    
print(Solution().strStr("mississippi","issip"))
