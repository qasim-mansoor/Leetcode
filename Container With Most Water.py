class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        maxA = 0
        righti = len(height) - 1
        lefti = 0

        while(righti != lefti):
            
            maxA = max(min(height[lefti], height[righti])*(righti - lefti), maxA)

            if(height[lefti] > height[righti]):
                righti -= 1
            else:
                lefti += 1
        
        return maxA


print(Solution().maxArea([5,6]))