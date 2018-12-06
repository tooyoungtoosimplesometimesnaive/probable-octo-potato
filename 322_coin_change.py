class Solution:
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        if amount == 0:
            return 0

        dp = [[-1 for _ in range(amount + 1)] for _ in range(len(coins))]
        
        for j in range(1, amount + 1):
            if j >= coins[0] and j % coins[0] == 0:
                dp[0][j] = j // coins[0]
        
        for i in range(1, len(coins)):
            for j in range(1, amount + 1):
                if j == coins[i]:
                    dp[i][j] = 1
                elif j - coins[i] > 0:
                    if dp[i][j - coins[i]] == -1 and dp[i - 1][j] == -1:
                        continue
                    elif dp[i][j - coins[i]] == -1:
                        dp[i][j] = dp[i - 1][j]
                    elif dp[i - 1][j] == -1:
                        dp[i][j] = dp[i][j - coins[i]] + 1
                    else:
                        dp[i][j] = min(dp[i - 1][j], dp[i][j - coins[i]] + 1)
                else:
                    dp[i][j] = dp[i - 1][j]
        
        return dp[len(coins) - 1][amount]


