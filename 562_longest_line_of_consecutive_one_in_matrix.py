class Solution:
    def longestLine(self, M):
        """
        :type M: List[List[int]]
        :rtype: int
        """
        row = len(M)
        if row == 0:
            return 0

        col = len(M[0])

        dp = [[[0 for _ in range(4)] for _ in range(col)] for _ in range(row)]
        
        # induction rule:
        # dp[i][j][k] -> k = 0 horizontal
        #             -> k = 1 vertical
        #             -> k = 2 diagonal
        #             -> k = 3 anti-diagonal

        result = 0
        for i in range(row):
            for j in range(col):
                if M[i][j] == 0:
                    continue
                for k in range(4):
                    dp[i][j][k] = 1
                if j > 0:
                    dp[i][j][0] += dp[i][j - 1][0]
                if i > 0:
                    dp[i][j][1] += dp[i - 1][j][1]
                if i > 0 and j > 0:
                    dp[i][j][2] += dp[i - 1][j - 1][2]
                if i > 0 and j < col - 1:
                    dp[i][j][3] += dp[i - 1][j + 1][3]
                
                result = max(result, dp[i][j][0], dp[i][j][1], dp[i][j][2], dp[i][j][3])
        
        return result

