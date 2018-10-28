class UnionFind:
    def __init__(self, size):
        self.ids = [i for i in range(size)]
        self.sizes = [1 for i in range(size)]
        self.count = 0

    def root(self, a):
        root = a
        while self.ids[root] != root:
            root = self.ids[root]
        
        while a != root:
            t = self.ids[a]
            self.ids[a] = root
            a = t
        return root

    def find(self, a, b):
        return self.root(a) == self.root(b)
    
    def union(self, a, b):
        root_a = self.root(a)
        root_b = self.root(b)

        if root_a != root_b:
            self.count -= 1
        else:
            return

        if self.sizes[root_a] >= self.sizes[root_b]:
            self.ids[root_b] = root_a
            self.sizes[root_a] += self.sizes[root_b]
        else:
            self.ids[root_a] = root_b
            self.sizes[root_b] += self.sizes[root_a]

class Solution:
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if len(grid) == 0:
            return 0
        row = len(grid)
        col = len(grid[0])
        uf = UnionFind(row * col)
        
        for i in range(row):
            for j in range(col):
                if grid[i][j] == '0':
                    continue
                uf.count += 1
                index = i * col + j
                # up
                if i > 0 and grid[i - 1][j] == '1':
                    uf.union(index, index - col)
                # left
                if j > 0 and grid[i][j - 1] == '1':
                    uf.union(index, index - 1)
        return uf.count


# Take 2: DFS:
class Solution:
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        row = len(grid)
        if row == 0:
            return 0
        col = len(grid[0])
        result = 0
        visited = [[False for _ in range(col)] for _ in range(row)]
        for i in range(row):
            for j in range(col):
                if grid[i][j] == '1' and not visited[i][j]:
                    visited[i][j] = True
                    result += 1
                    self.count(grid, i, j, visited)

        return result

    def count(self, grid, i, j, visited):
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        row = len(grid)
        col = len(grid[0])
        for dx, dy in directions:
            x = i + dx
            y = j + dy
            if x >= 0 and x < row and y >= 0 and y < col and grid[i][j] == '1' and not visited[x][y]:
                visited[x][y] = True
                self.count(grid, x, y, visited)

