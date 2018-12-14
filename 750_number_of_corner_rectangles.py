class Solution:
    def countCornerRectangles(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        row = len(grid)
        if row <= 1:
            return 0
        col = len(grid[0])
        
        matrix = []
        for i in range(row):
            index_row = []
            for j in range(col):
                if grid[i][j] == 1:
                    index_row.append(j)
            if len(index_row) > 0:
                matrix.append(index_row)
        
        result = 0
        count_map = {}
        for k in range(len(matrix)):
            l = len(matrix[k])
            for i in range(l - 1):
                for j in range(i + 1, l):
                    count_map[(matrix[k][i], matrix[k][j])] = count_map.get((matrix[k][i], matrix[k][j]), 0) + 1

        for k, v in count_map.items():
            result += v * (v - 1) // 2
        return result

