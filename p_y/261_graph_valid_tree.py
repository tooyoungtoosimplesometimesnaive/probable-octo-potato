class UnionFind:
    def __init__(self, size):
        self.ids = [i for i in range(size)]
    
    def root(self, a):
        root = a
        while root != self.ids[root]:
            root = self.ids[root]
        
        while root != self.ids[a]:
            t = self.ids[a]
            self.ids[a] = root
            a = t
        return root
    
    def union(self, a, b):
        root_a = self.root(a)
        root_b = self.root(b)
        
        self.ids[root_b] = root_a

class Solution:
    def validTree(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: bool
        """
        uf = UnionFind(n)
        for e1, e2 in edges:
            if uf.root(e1) == uf.root(e2):
                return False
            else:
                uf.union(e1, e2)

        root = uf.root(0)
        for i in range(n):
            if root != uf.root(i):
                return False
        return True
