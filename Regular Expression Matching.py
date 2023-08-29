class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        idp = len(p)-1
        ids = len(s)-1
        star = False
        starval = ""

        while(idp >= 0 or ids >= 0):
            print(idp, ids)
            if(not star and idp < 0 and ids >= 0):
                return False
            if(p[idp] == '*' and idp >= 0):
                print("2")
                star = True
                starval = p[idp-1]
                idp -= 2
            elif(star and s[ids] == starval or starval == '.'):
                ids -= 1
            elif(star and s[ids] != starval or starval == '.'):
                star = False
            elif(p[idp] == '.'):
                s[ids] -= 1
            elif(p[idp] == s[ids]):
                print("1")
                idp -= 1
                ids -= 1
            elif(p[idp] != s[ids]):
                return False


        if(idp > 0 or ids > 0):
            return False
        else:
            return True

print(Solution().isMatch("aab","c*a*b"))