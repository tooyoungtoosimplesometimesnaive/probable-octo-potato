class Solution:
    def minSteps(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 1:
            return 0

        dp = [0 for i in range(n + 1)]
        dp[1] = 0

        for i in range(2, n + 1):
            min_val = 1000
            for j in range(1, i):
                if i % j == 0:
                    min_val = min(min_val, dp[j] + (i // j) - 1 + 1)
            dp[i] = min_val
        return dp[n]
