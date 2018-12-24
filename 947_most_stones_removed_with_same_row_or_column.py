class UnionFind:
    def __init__(self, size):
        self.sizes = [1 for _ in range(size)]
        self.ids = [i for i in range(size)]
        self.count = size
    
    def root(self, i):
        r = i
        while r != self.ids[r]:
            r = self.ids[r]

        while i != r:
            t = self.ids[i]
            self.ids[i] = r
            i = t

        return r

    def find(self, a, b):
        return self.root(a) == self.root(b)

    def union(self, a, b):
        root_a = self.root(a)
        root_b = self.root(b)
        
        if root_a == root_b:
            return

        # balancing
        if self.sizes[root_a] >= self.sizes[root_b]:
            self.ids[root_b] = root_a
            self.sizes[root_a] += self.sizes[root_b]
        else:
            self.ids[root_a] = root_b
            self.sizes[root_b] += self.sizes[root_a]

class Solution:
    def removeStones(self, stones):
        """
        :type stones: List[List[int]]
        :rtype: int
        """
        uf = UnionFind(20000)
        N = len(stones)

        for x, y in stones:
            uf.union(x, y + 10000)
        
        s = set()
        for x, y in stones:
            s.add(uf.root(x))

        return N - len(s)

