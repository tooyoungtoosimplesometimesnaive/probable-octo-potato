class Solution:
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        result = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                c = grid[i][j]
                if c == 0:
                    continue
                else:
                    result += self.calc_peri(i, j, grid)
        return result
                
    def calc_peri(self, i, j, grid):
        rows = len(grid)
        cols = len(grid[0])
        p = 0
        if i == 0: p += 1
        if i == rows - 1: p += 1
        if j == 0: p += 1
        if j == cols - 1: p += 1
        
        if i + 1 < rows and grid[i + 1][j] == 0:
            p += 1
        if i - 1 >= 0 and grid[i - 1][j] == 0:
            p += 1
        if j + 1 < cols and grid[i][j + 1] == 0:
            p += 1
        if j - 1 >= 0 and grid[i][j - 1] == 0:
            p += 1
        return p
