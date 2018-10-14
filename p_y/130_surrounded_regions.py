class UnionFind:
    def __init__(self, size):
        self.ids = [i for i in range(size)]
        self.sizes = [1 for i in range(size)]
    def root(self, a):
        root = a
        while root != self.ids[root]:
            root = self.ids[root]
        # path compression:
        while self.ids[a] != root:
            t = self.ids[a]
            self.ids[a] = root
            a = t
        return root
    def union(self, a, b):
        root_a = self.root(a)
        root_b = self.root(b)
        
        if self.sizes[root_a] >= self.sizes[root_b]:
            self.ids[root_b] = root_a
            self.sizes[root_a] += self.sizes[root_b]
        else:
            self.ids[root_a] = root_b
            self.sizes[root_b] += self.sizes[root_a]

class Solution:
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        row = len(board)
        if row == 0:
            return
        col = len(board[0])
        
        uf = UnionFind(row * col)
        for i in range(row):
            for j in range(col):
                if board[i][j] == 'O':
                    index = i * col + j
                    if i > 0 and board[i - 1][j] == 'O':
                        uf.union(index, index - col)
                    if j > 0 and board[i][j - 1] == 'O':
                        uf.union(index, index - 1)
        
        unsurrounded_roots = set()
        for i in range(row):
            if board[i][0] == 'O':
                unsurrounded_roots.add(uf.root(i * col))
            if board[i][col - 1] == 'O':
                unsurrounded_roots.add(uf.root(i * col + col - 1))
        for j in range(col):
            if board[0][j] == 'O':
                unsurrounded_roots.add(uf.root(j))
            if board[row - 1][j] == 'O':
                unsurrounded_roots.add(uf.root( (row-1) * col + j))

        for i in range(row):
            for j in range(col):
                index = i * col + j
                if board[i][j] == 'O' and uf.root(index) not in unsurrounded_roots:
                    board[i][j] = 'X'

                    
