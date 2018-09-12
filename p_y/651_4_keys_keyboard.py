class Solution:
    def maxA(self, N):
        """
        :type N: int
        :rtype: int
        """
        if N <= 3:
            return N
        dp = [0 for i in range(N + 1)]
        dp[1] = 1
        dp[2] = 2
        dp[3] = 3
        #dp[4] = 4
        for i in range(4, N + 1):
            #press key 1
            max_val = dp[i - 1] + 1
            for j in range(2, i - 1):
                #print(j)
                max_val = max(max_val, dp[j - 1] * (i - j - 1 + 1))
            #print(max_val)
            dp[i] = max_val
            #print("----")
        return dp[N]
