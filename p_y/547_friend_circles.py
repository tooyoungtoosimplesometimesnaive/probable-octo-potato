class UnionFind:
    def __init__(self, size):
        self.ids = [i for i in range(size)]
        self.sizes = [1 for i in range(size)]
        self.count = 0
    
    def root(self, a):
        root = a
        while self.ids[root] != root:
            root = self.ids[root]
        
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
    def findCircleNum(self, M):
        """
        :type M: List[List[int]]
        :rtype: int
        """
        N = len(M)
        uf = UnionFind(N)
        uf.count = N
        for i in range(N):
            for j in range(i, N):
                if M[i][j] == 1:
                    uf.union(i, j)
                #print("{} {}".format(i, j))
        
        return uf.count

# Take 2: DFS:
class Solution:
    def findCircleNum(self, M):
        """
        :type M: List[List[int]]
        :rtype: int
        """
        n = len(M)
        visited = [False for _ in range(n)]
        number = 0
        for i in range(n):
            if not visited[i]:
                number += 1
                #visited[i] = True
                self.dfs(M, i, visited)

        return number

    def dfs(self, M, i, visited):
        for j in range(len(M)):
            if M[i][j] == 1 and not visited[j]:
                visited[j] = True
                self.dfs(M, j, visited)
