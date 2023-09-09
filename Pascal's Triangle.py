class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        res = [[1]]
        for i in range(1,numRows): # 1,2,3,4
            subres = []
            for j in range(i + 1):
                if(j == 0):
                    subres.append(1)
                    continue
                
                if(j >= len(res[i - 1])):
                    subres.append(1)
                    continue

                subres.append(res[i - 1][j] + res[i - 1][j-1])
            
            res.append(subres)
        return res