class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        def checker(row, col):
            grid[row][col] = "0"

            # to send down
            if row + 1 < len(grid) and grid[row+1][col] == "1":
                checker(row+1, col)
            
            #to send right
            if col + 1 < len(grid[0]) and grid[row][col+1] == "1":
                checker(row, col+1)

            #to send up
            if row - 1 >= 0 and grid[row-1][col] == "1":
                checker(row-1, col)

            # to send left
            if col - 1 >= 0 and grid[row][col-1] == "1":
                checker(row, col-1)

        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if(grid[i][j] == "1"):
                    count += 1
                    checker(i,j)

        return count
        