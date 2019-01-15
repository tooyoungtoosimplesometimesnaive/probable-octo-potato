class Solution(object):
    def splitArray(self, nums, m):
        """
        :type nums: List[int]
        :type m: int
        :rtype: int
        """
        n = len(nums)
        dp = [[float('inf') for _ in range(m + 1)] for _ in range(n + 1)]
        sub = [0 for _ in range(n + 1)]
        for i in range(n):
            sub[i + 1] = sub[i] + nums[i]

        dp[0][0] = 0

        for i in range(1, n + 1):
            for j in range(1, m + 1):
            
                for k in range(i):
                    dp[i][j] = min(dp[i][j], max(dp[k][j - 1], sub[i] - sub[k]))

        return dp[n][m]
