class Solution(object):
    def change(self, amount, coins):
        """
        :type amount: int
        :type coins: List[int]
        :rtype: int
        """
        dp = [[0 for _ in range(amount + 1)] for _ in range(1 + len(coins))]
        dp[0][0] = 1
        for i in range(1, 1 + len(coins)):
            dp[i][0] = 1
            for j in range(1, amount + 1):
                dp[i][j] = dp[i - 1][j]
                if j - coins[i - 1] >= 0:
                    dp[i][j] += dp[i][j - coins[i - 1]]
        # print(dp)
        return dp[len(coins)][amount]

