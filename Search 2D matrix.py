class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        l = 0
        r = (len(matrix) * len(matrix[0])) - 1

       

        while l <= r:
            m = (r + l) // 2 # 5
            row = m // len(matrix[0])
            col = m % len(matrix[0])
            print(m, row, col)
            
            if matrix[row][col] == target:
                return True
            elif matrix[row][col] > target:
                r = m - 1
            else:
                l = m + 1

        return False
                
        