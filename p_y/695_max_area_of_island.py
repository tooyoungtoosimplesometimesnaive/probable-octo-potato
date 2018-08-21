class Solution:
    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        visited = [[a == 0 for a in row] for row in grid]
        #print(visited)
        maxi = 0
        for i in range(0, len(grid)):
            for j in range(0, len(grid[0])):
                if not visited[i][j]:
                    area = self.calc(grid, visited, i, j)
                    if area > maxi:
                        maxi = area
        return maxi
    def calc(self, grid, visited, i, j):
        if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]) or visited[i][j]:
            return 0
        visited[i][j] = True
        return 1 + self.calc(grid, visited, i + 1, j) + self.calc(grid, visited, i - 1, j) + self.calc(grid, visited, i, j + 1) + self.calc(grid, visited, i, j - 1)

