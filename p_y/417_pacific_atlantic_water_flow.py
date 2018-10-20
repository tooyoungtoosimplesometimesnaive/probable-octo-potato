class Solution:
    def __init__(self):
        self.directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        self.row = 0
        self.col = 0
    def pacificAtlantic(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        p_set = set()
        a_set = set()
        
        self.row = len(matrix)
        if self.row == 0:
            return []
        self.col = len(matrix[0])
        if self.col == 0:
            return []
        
        for i in range(self.row):
            self.dfs(matrix, i, 0, p_set) # first column
            self.dfs(matrix, i, self.col -1, a_set) # last column
        
        for j in range(self.col):
            self.dfs(matrix, 0, j, p_set) # 1st row
            self.dfs(matrix, self.row - 1, j, a_set) #last row
        
        result_set = p_set & a_set
        print(result_set)
        
        return list(result_set)
        
    def dfs(self, matrix, i, j, visited_set):
        visited_set.add((i, j))
        
        for dx, dy in self.directions:
            if i + dx >= self.row or i + dx < 0 or j + dy >= self.col or j + dy < 0 or (i + dx, j + dy) in visited_set:
                continue
            if matrix[i + dx][j + dy] >= matrix[i][j]:
                self.dfs(matrix, i + dx, j + dy, visited_set)
        
        
