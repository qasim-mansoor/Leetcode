class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """

        count = 1
        numstr = "1"
        
        while count < n:
            
            temp = ""
            
            ph = None
            i = 0
            c = 0

            while i < len(numstr):
                if ph != numstr[i]:
                    if ph:
                        temp = temp + (str(c) + ph)
                    ph = numstr[i]
                    c = 1
                else:
                    c += 1
                
                i += 1
            
            temp = temp + (str(c) + ph)

            numstr = temp
            count += 1
        
        return numstr
                