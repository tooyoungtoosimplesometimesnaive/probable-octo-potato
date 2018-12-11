class Solution:
    def maxKilledEnemies(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        row = len(grid)
        if row == 0:
            return 0
        col = len(grid[0])
        up = [[0 for _ in range(col)] for _ in range(row)]
        down = [[0 for _ in range(col)] for _ in range(row)]
        left = [[0 for _ in range(col)] for _ in range(row)]
        right = [[0 for _ in range(col)] for _ in range(row)]
        
        for i in range(row):
            for j in range(col):
                if j == 0:
                    left[i][j] = 1 if grid[i][j] == 'E' else 0
                    continue
                if grid[i][j] == 'W':
                    left[i][j] = 0
                elif grid[i][j] == 'E':
                    left[i][j] = left[i][j - 1] + 1
                else:
                    left[i][j] = left[i][j - 1]
        
        for i in range(row):
            for j in range(col - 1, -1, -1):
                if j == col - 1:
                    right[i][j] = 1 if grid[i][j] == 'E' else 0
                    continue
                if grid[i][j] == 'W':
                    right[i][j] = 0
                elif grid[i][j] == 'E':
                    right[i][j] = right[i][j + 1] + 1
                else:
                    right[i][j] = right[i][j + 1]
        
        for j in range(col):
            for i in range(row):
                if i == 0:
                    up[i][j] = 1 if grid[i][j] == 'E' else 0
                    continue
                if grid[i][j] == 'W':
                    up[i][j] = 0
                elif grid[i][j] == 'E':
                    up[i][j] = up[i - 1][j] + 1
                else:
                    up[i][j] = up[i - 1][j]
        for j in range(col):
            for i in range(row - 1, -1, -1):
                if i == row - 1:
                    down[i][j] = 1 if grid[i][j] == 'E' else 0
                    continue
                if grid[i][j] == 'W':
                    down[i][j] = 0
                elif grid[i][j] == 'E':
                    down[i][j] = down[i + 1][j] + 1
                else:
                    down[i][j] = down[i + 1][j]
    
        result = 0
        for i in range(row):
            for j in range(col):
                if grid[i][j] == '0':
                    result = max(result, up[i][j] + down[i][j] + left[i][j] + right[i][j])
        
        return result

