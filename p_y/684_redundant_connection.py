class UnionFind:
    def __init__(self, size):
        self.ids = [i for i in range(size)]
        self.sizes = [1 for i in range(size)]
    
    def root(self, a):
        root = a
        while root != self.ids[root]:
            root = self.ids[root]
        
        # path:
        while a != self.ids[root]:
            t = self.ids[a]
            self.ids[a] = root
            a = t
        return root
    
    def find(self, a, b):
        return self.root(a) == self.root(b)
    
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
    def findRedundantConnection(self, edges):
        """
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        size = 0
        for v1, v2 in edges:
            size = max(size, v1, v2)
        uf = UnionFind(size + 1)
        
        rv1 = 0
        rv2 = 0
        for v1, v2 in edges:
            if uf.root(v1) != uf.root(v2):
                uf.union(v1, v2)
            else:
                rv1 = min(v1, v2)
                rv2 = max(v1, v2)

        return [rv1, rv2]        
            
