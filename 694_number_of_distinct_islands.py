class Solution:
    def numDistinctIslands(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        row = len(grid)
        col = len(grid[0])
        
        result = set()
        
        visited = [[False for _ in range(col)] for _ in range(row)]
        
        for i in range(row):
            for j in range(col):
                if grid[i][j] == 1:
                    island = []
                    self.dfs(grid, visited, i, j, 'o', island)
                    if len(island) > 0:
                        island_str = "".join(island)
                        result.add(island_str)
        #print(result)
        return len(result)
        
    def dfs(self, grid, visited, i, j, d, island):
        row = len(grid)
        col = len(grid[0])
        if i >= 0 and i < row and j >= 0 and j < col and grid[i][j] == 1 and not visited[i][j]:
            visited[i][j] = True
            island.append(d)
            self.dfs(grid, visited, i + 1, j, 'd', island)
            self.dfs(grid, visited, i - 1, j, 'u', island)
            self.dfs(grid, visited, i, j + 1, 'r', island)
            self.dfs(grid, visited, i, j - 1, 'l', island)
            island.append('b')
    

