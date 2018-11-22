class Solution(object):
    def numWays(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        # dp[i][k] : number of ways paint 0-i with i painted with color k
        # dp[i][k] = dp[i-2][c1] + dp[i-2][c2]... + sum(dp[i-1][0..k])
        # dp[i][0] = dp[i-2][1] + ... + dp[i-2][k] + sum(dp[i-1][0..k])
        # dp[i][1] = dp[i-2][0] + ... + dp[i-2][k] + sum(dp[i-1][0..k])
        
        # dp[i][0] == dp[i][1] == dp[i][2] == .. == dp[i][k]
        
        # dp[i] = (k-1) * dp[i-2] + (k - 1)* dp[i-1]
        
        if n == 0 or k == 0:
            return 0
        if n == 1:
            return k
        if n == 2:
            return k * k
        
        # dp = [0] * n
        # dp[0] = k
        # dp[1] = k * k
        
        num1 = k
        num2 = k * k
        
        for i in range(2, n):
            # dp[i] = dp[i - 2] * (k - 1) + dp[i - 1] * (k - 1)
            num3 = (k - 1) * num1 + (k - 1) * num2
            num1 = num2
            num2 = num3
        
        return num2

        
