class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        
        stack = []

        for brac in s:
            if brac in [')', ']', '}']:
                if stack:
                    res = stack.pop()
                    if (brac == ')' and res != '(') or (brac == ']' and res != '[') or (brac == '}' and res != '{'):
                        return False
                else:
                    return False
            else:
                stack.append(brac)
        
        if not stack:
            return True
        else:
            return False
    
print(Solution().isValid("("))