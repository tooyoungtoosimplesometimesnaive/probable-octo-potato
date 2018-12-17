class UnionFind:
    def __init__(self, size):
        self.ids = [i for i in range(size)]
        self.sizes = [1 for i in range(size)]
    
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
    
    # a attached to b, b is the new root
    def union(self, a, b):
        root_a = self.root(a)
        root_b = self.root(b)
        
        if root_a == root_b:
            return
        self.ids[root_a] = root_b
        self.sizes[root_b] += self.sizes[root_a]

class Solution:
    def hitBricks(self, grid, hits):
        """
        :type grid: List[List[int]]
        :type hits: List[List[int]]
        :rtype: List[int]
        """
        self.row = len(grid)
        self.col = len(grid[0])

        # 0 means attached to roof
        uf = UnionFind(self.row * self.col + 1)

        for x, y in hits:
            if grid[x][y] == 1:
                grid[x][y] = 2
        
        for i in range(self.row):
            for j in range(self.col):
                if grid[i][j] == 1:
                    self.union_around(grid, uf, i, j)

        count = uf.sizes[uf.root(0)]
        result = []
        for x, y in hits[::-1]:
            if grid[x][y] == 2:
                self.union_around(grid, uf, x, y)
                grid[x][y] = 1
            
            new_size = uf.sizes[uf.root(0)]
            falling_bricks = new_size - count - 1 if new_size > count else 0
            result.append(falling_bricks)
            count = new_size
        
        return result[::-1]

    def union_around(self, grid, uf, x, y):
        if x - 1 >= 0 and grid[x - 1][y] == 1:
            uf.union(x * self.col + y + 1, (x - 1) * self.col + y + 1)
        if x + 1 < self.row and grid[x + 1][y] == 1:
            uf.union(x * self.col + y + 1, (x + 1) * self.col + y + 1)
        if y - 1 >= 0 and grid[x][y - 1] == 1:
            uf.union(x * self.col + y + 1, x * self.col + y)
        if y + 1 < self.col and grid[x][y + 1] == 1:
            uf.union(x * self.col + y + 1, x * self.col + y + 1 + 1)
        
        if x == 0:
            uf.union(x * self.col + y + 1, 0)



