class Solution:
    def projectionArea(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        x = len(grid)
        y = len(grid[0])
        
        side1 = 0
        for i in range(0, x):
            m = 0
            for j in range(0, y):
                if grid[i][j] > m:
                    m = grid[i][j]
            side1 += m
            
        side2 = 0
        for j in range(0, y):
            m = 0
            for i in range(0, x):
                if grid[i][j] > m:
                    m = grid[i][j]
            side2 += m
        
        bottom = 0
        for i in range(0, x):
            for j in range(0, y):
                if grid[i][j] != 0:
                    bottom += 1
        
        return side1 + side2 + bottom

