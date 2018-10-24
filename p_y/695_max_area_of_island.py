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


# Take 2: BFS
class Solution:
    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        visited = [[a == 0 for a in row] for row in grid]
        row = len(grid)
        if row == 0:
            return 0
        col = len(grid[0])
        #print(visited)

        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        result = 0
        for i in range(row):
            for j in range(col):
                if not visited[i][j]:
                    q = [(i, j)]
                    visited[i][j] = True
                    area = 0
                    while q:
                        x, y = q.pop(0)
                        area += 1
                        for dx, dy in directions:
                            if x+dx >= 0 and x+dx < row and y+dy >= 0 and y+dy < col and not visited[x+dx][y+dy]:
                                visited[x + dx][y + dy] = True
                                q.append((x + dx, y + dy))
                    result = max(result, area)
        return result

