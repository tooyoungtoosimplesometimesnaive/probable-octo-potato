class Solution:
    def maxCoins(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if n == 0:
            return 0
        
        nums = [1] + nums + [1]
        
        coins = [[0 for _ in range(len(nums))] for _ in range(len(nums))]
        
        
        # coins[i][j] => max coins from index i to j
        # answer : coins[1][n]

        
        for length in range(1, n + 1): # 1 - n
            for i in range(1, n - length + 1 + 1): # 1 to n - length + 1
                j = i + length - 1
                for k in range(i, j + 1):
                    coins[i][j] = max(coins[i][j], nums[i - 1] * nums[k] * nums[j + 1] + coins[i][k -1] + coins[k+1][j])
        
        return coins[1][n]


