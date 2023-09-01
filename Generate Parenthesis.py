class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        pars = []

        def rec(s, ob, cb):
            if ob == n and cb == n:
                if s not in pars:
                    pars.append(s)
            
            if ob < n and cb < ob:
                rec(s+"(", ob+1, cb)
                rec(s+")", ob, cb+1)

            if(ob < n):
                rec(s+"(", ob+1, cb)
            
            if(cb < ob):
                rec(s+")", ob, cb+1)
            
        rec("", 0, 0)
        print(pars)

print(Solution().generateParenthesis(2))
        