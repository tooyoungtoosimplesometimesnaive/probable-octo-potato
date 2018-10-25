class Solution:
    def __init__(self):
        self.directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
    def updateMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        row = len(matrix)
        col = len(matrix[0])
        #print(row)
        #print(col)
        q = []
        for i in range(row):
            for j in range(col):
                if matrix[i][j] == 0:
                    q.append((i, j))
                else:
                    matrix[i][j] = float('Inf')
        while q:
            x, y = q.pop(0)
            for dx, dy in self.directions:
                xx = x + dx
                yy = y + dy
                if xx < 0 or xx >= row or yy < 0 or yy >= col or matrix[xx][yy] <= matrix[x][y] + 1:
                    continue
                q.append((xx, yy))
                matrix[xx][yy] = matrix[x][y] + 1

        #print(matrix)
        return matrix
