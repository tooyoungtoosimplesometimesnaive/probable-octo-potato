class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        row = len(obstacleGrid)
        if row == 0:
            return 0

        col = len(obstacleGrid[0])
        
        dp = [[0 for _ in range(col)] for _ in range(row)]

        if obstacleGrid[0][0] == 1:
            return 0
        
        dp[0][0] = 1
        for i in range(1, col):
            dp[0][i] = dp[0][i - 1] if obstacleGrid[0][i] != 1 else 0
        
        for i in range(1, row):
            dp[i][0] = dp[i - 1][0] if obstacleGrid[i][0] != 1 else 0
            
        
        for i in range(1, row):
            for j in range(1, col):
                if obstacleGrid[i][j] != 1:
                    dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
        
        return dp[row - 1][col - 1]
            

