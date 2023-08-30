class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        lwall = None
        rwall = None
        tempmax = 0
        maxlen = 0
        tempmaxi = None

        for i in range(len(height)):
            if not lwall:
                lwall = i
                continue
            
            if(height[i] > height[lwall]):
                lwall = i
                maxlen = max(tempmax, maxlen)
                tempmax = 0
                tempmaxi = None
                continue
            
            if(not rwall and i>lwall+1 and height[i] > height[i-1]):
                rwall = i
                maxlen = max(min(height[lwall] - height[tempmaxi], height[rwall] - height[tempmaxi]), maxlen)
            
            if(height[i] < height[lwall] and not rwall):
                if(height[lwall] - height[i] > tempmax):
                    tempmax = height[lwall] - height[i]
                    tempmaxi = i  
            
            if(lwall and rwall and min(height[lwall] - height[i], height[rwall] - height[i]) > maxlen):
                maxlen = min(height[lwall] - height[i], height[rwall] - height[i])
                
            if(rwall):
                maxlen = max(tempmax, maxlen)
        
        return maxlen
               
            


print(Solution().trap([0,1,0,2,1,0,1,3,2,1,2,1]))
# lwall                        
# rwall                              
# tempmax = 
# maxlen = 