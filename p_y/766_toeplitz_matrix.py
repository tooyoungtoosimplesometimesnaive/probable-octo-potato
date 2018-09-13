class Solution:
    def isToeplitzMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: bool
        """
        row = matrix[0]
        for i in range(1, len(matrix)):
            row = [matrix[i][0]] + row[0:-1]
            if row != matrix[i]:
                return False
            row = matrix[i]
        return True
