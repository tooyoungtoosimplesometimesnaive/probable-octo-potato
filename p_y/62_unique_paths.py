class Solution:
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        b = [[0 for i in range(n)] for j in range(m)]
        #print(b)
        for i in range(n):
            b[0][i] = 1
        for j in range(m):
            #print(j)
            b[j][0] = 1
        
        for i in range(1, m):
            for j in range(1, n):
                b[i][j] = b[i - 1][j] + b[i][j - 1]
        return b[m - 1][n - 1]
