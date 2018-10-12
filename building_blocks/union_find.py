
class UnionFind:
    def __init__(self, size):
        self.ids = [i for i in range(size)]
        self.sizes = [1 for i in range(size)]

    def root(self, a):
        root = a
        while self.ids[root] != root:
            root = self.ids[root]

        # Path compression
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

        if self.sizes[root_a] >= self.sizes[root_b]:
            # merge b into a:
            self.ids[root_b] = root_a
            self.sizes[root_a] += self.sizes[root_b]
        else:
            self.ids[root_a] = root_b
            self.sizes[root_b] += self.sizes[root_a]


if __name__ == '__main__':
    print("Hello world")
    uf = UnionFind(10)
    uf.union(3, 4)
    print(uf.ids)
