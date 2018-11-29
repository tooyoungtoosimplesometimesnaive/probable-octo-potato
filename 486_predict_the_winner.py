class Solution:
    def PredictTheWinner(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        """
        dp[i][j] = A's max score can get from index i to j, inclusive
        dp[i][j] = 
            case1: pick i
                min(dp[i + 2][j], dp[i + 1][j - 1]) + nums[i]   -> B pick the minimum
            case2: pick j
                min(dp[i][j - 2], dp[i + 1][j - 1]) + nums[j]
        dp[i][j] = max(case1, case2)
        
        result = dp[0][len(nums) - 1]
        
        x  x  x
           x  x
              x
        base case dp[i][i] = nums[i], dp[i][i + 1] = max(nums[i],nums[i+1])
        """
        
        dp = [[0 for _ in range(len(nums))] for _ in range(len(nums))]
        
        for i in range(len(nums)):
            dp[i][i] = nums[i]
            if i != len(nums) - 1:
                dp[i][i + 1] =  max(nums[i], nums[i + 1])
        
        
        for i in range(len(nums) - 3, -1, -1):
            for j in range(i + 2, len(nums)):
                dp[i][j] = max(min(dp[i + 2][j], dp[i + 1][j - 1]) + nums[i], min(dp[i][j - 2], dp[i + 1][j - 1]) + nums[j])
        
        #print(dp)
        return dp[0][len(nums) - 1] >= sum(nums) - dp[0][len(nums) - 1]

