class UnionFind:
    def __init__(self, size):
        self.ids = [i for i in range(size)]
        self.sizes = [1 for i in range(size)]
        self.count = 0
    
    def root(self, a):
        root = a
        while self.ids[root] != root:
            root = self.ids[root]

        # path compression
        while self.ids[a] != root:
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
    def numIslands2(self, m, n, positions):
        """
        :type m: int
        :type n: int
        :type positions: List[List[int]]
        :rtype: List[int]
        """
        result = []
        
        # m is row, n is col
        uf = UnionFind(m * n)
        board = [[0 for i in range(n)] for j in range(m)]
        for x, y in positions:
            index = x * n + y
            board[x][y] = 1
            uf.count += 1
            # four directions:
            if x > 0 and board[x - 1][y] == 1:
                uf.union(index, index - n)
            if y > 0 and board[x][y - 1] == 1:
                uf.union(index, index - 1)
            if x < m - 1 and board[x + 1][y] == 1:
                uf.union(index, index + n)
            if y < n - 1 and board[x][y + 1] == 1:
                uf.union(index, index + 1)
            result.append(uf.count)
        
        return result

