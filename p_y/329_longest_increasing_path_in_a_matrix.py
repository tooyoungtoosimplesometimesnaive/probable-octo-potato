class Solution:
    def __init__(self):
        self.result = 0
        self.row = 0
        self.col = 0
    def longestIncreasingPath(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return 0
        self.row = len(matrix)
        self.col = len(matrix[0])
                
        mem = [[0 for _ in range(self.col)] for _ in range(self.row)]
        result = 0
        for i in range(self.row):
            for j in range(self.col):
                result = max(result, self.dfs(matrix, i, j, mem))
        return result
                
    def dfs(self, matrix, i, j, mem):
        if mem[i][j] > 0:
            return mem[i][j]

        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        res = 1
        for dx, dy in directions:
            if i + dx < 0 or i + dx >= self.row or j + dy < 0 or j + dy >= self.col or matrix[i + dx][j + dy] <= matrix[i][j]:
                continue
            l = 1 + self.dfs(matrix, i + dx, j + dy, mem)
            res = max(res, l)
        mem[i][j] = res
        return res


