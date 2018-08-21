class DSU:
    def __init__(self, N):
        self.par = [a for a in range(N)]

    def find(self, x):
        #print(x)
        if self.par[x] != x:
            self.par[x] = self.find(self.par[x])
        return self.par[x]

    def union(self, x, y):
        self.par[self.find(x)] = self.find(y)
        

class Solution:
    def areSentencesSimilarTwo(self, words1, words2, pairs):
        """
        :type words1: List[str]
        :type words2: List[str]
        :type pairs: List[List[str]]
        :rtype: bool
        """
        if len(words1) != len(words2): return False

        index = {}
        count = 0
        dsu = DSU(2 * len(pairs))
        for [p1, p2] in pairs:
            #print("p1={},p2={}".format(p1, p2))
            if p1 not in index:
                index[p1] = count
                count += 1
            if p2 not in index:
                index[p2] = count
                count += 1
            dsu.union(index[p1], index[p2])
        return all(w1 == w2 or w1 in index and w2 in index and dsu.find(index[w1]) == dsu.find(index[w2]) for w1, w2 in zip(words1, words2))


# Another :
class DSU:
    def __init__(self, N):
        self.par = [a for a in range(N)]

    def find(self, x):
        #print(x)
        #if self.par[x] != x:
        #    self.par[x] = self.find(self.par[x])

        while x != self.par[x]:
            x = self.par[x]

        return x

    def union(self, x, y):
        self.par[self.find(x)] = self.find(y)

