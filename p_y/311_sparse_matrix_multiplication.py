class Solution:
    def multiply(self, A, B):
        """
        :type A: List[List[int]]
        :type B: List[List[int]]
        :rtype: List[List[int]]
        """
        row_A = len(A)
        col_A = len(A[0])
        row_B = len(B)
        col_B = len(B[0])
        # col_A == row_B
        # row_A * col_B
        result = [[0 for i in range(col_B)] for j in range(row_A)]

        for i in range(row_A):
            for k in range(col_A):
                if A[i][k] != 0:
                    for j in range(col_B):
                        if B[k][j] != 0:
                            result[i][j] += A[i][k] * B[k][j]
        
        return result
