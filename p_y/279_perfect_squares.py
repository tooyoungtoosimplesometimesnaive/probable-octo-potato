# This is TLE:
class Solution:
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0: return 0
        dp = [i for i in range(n + 1)]
        dp[1] = 1
        for i in range(1, n + 1): # i from 1 to n
            for j in range(i + 1):
                if int((i - j)**0.5) * int((i - j)**0.5) == i - j:
                    dp[i] = min(dp[i], dp[j] + 1)
        return dp[n]


