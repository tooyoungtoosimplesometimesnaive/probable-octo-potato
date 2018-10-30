class Solution(object):
    def __init__(self):
        self.crossing = {
            (1, 9): 5,
            (9, 1): 5,
            (2, 8): 5,
            (8, 2): 5,
            (3, 7): 5,
            (7, 3): 5,
            (1, 3): 2,
            (3, 1): 2,
            (4, 6): 5,
            (6, 4): 5,
            (7, 9): 8,
            (9, 7): 8,
            (1, 7): 4,
            (7, 1): 4,
            (3, 9): 6,
            (9, 3): 6
        }
        #self.result = 0
    def numberOfPatterns(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        visited = {1}
        r1 = 4 * self.dfs(1, m, n, visited)
        visited = {2}
        r2 = 4 * self.dfs(2, m, n, visited)
        visited = {5}
        r5 = self.dfs(5, m, n, visited)
        
        return r1 + r2 + r5
        
    def dfs(self, start, m, n, visited):
        result = 0
        if len(visited) >= m:
            result += 1
            if len(visited) == n:
                return result

        for i in range(1, 10):
            if i in visited:
                continue
            if (start, i) in self.crossing and self.crossing[(start, i)] not in visited:
                continue
            visited.add(i)
            result += self.dfs(i, m, n, visited)
            visited.remove(i)
        return result

