class Solution:
    def numDistinct(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: int
        """
        # dp[i][j]: distinct num of s[0..i-1] and t[0..j-1]
        # dp[i][j] = dp[i - 1][j] : s[i - 1] not contribute to the number
        #           + dp[i - 1][j - 1] if s[i-1] == t[j-1]
        # dp[i][j] = 0: i < j
        # dp[i][0] = 1
        # dp[0][j] = 0
        if len(s) < len(t):
            return 0

        dp = [[0 for _ in range(len(t) + 1)] for _ in range(len(s) + 1)]
        dp[0][0] = 1

        for i in range(1, len(s) + 1):
            dp[i][0] = 1
            for j in range(1, len(t) + 1):
                dp[i][j] = dp[i - 1][j]
                if s[i - 1] == t[j - 1]:
                    dp[i][j] += dp[i - 1][j - 1]
        
        #print(dp)
        return dp[len(s)][len(t)]

