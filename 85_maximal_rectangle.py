# On3, TLE
class Solution:
    def maximalRectangle(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        row = len(matrix)
        if row == 0:
            return 0
        col = len(matrix[0])
        result = 0
        prefix_sum = [[0 for _ in range(col)] for _ in range(row + 1)]
        for j in range(col):
            for i in range(1, row + 1):
                prefix_sum[i][j] = prefix_sum[i - 1][j] + int(matrix[i - 1][j])
        
        for i in range(row):
            for j in range(i, row):
                row_sum = [prefix_sum[j + 1][k] - prefix_sum[i][k] for k in range(col)]
                #print(row_sum, i, j)
                h = j - i + 1
                row_sum[0] = 1 if row_sum[0] == h else 0
                w = row_sum[0]
                for k in range(1, col):
                    if row_sum[k] == h:
                        row_sum[k] = 1 + row_sum[k - 1]
                    else:
                        row_sum[k] = 0
                    w = max(w, row_sum[k])
                    
                result = max(result, h * w)
                
        return result

