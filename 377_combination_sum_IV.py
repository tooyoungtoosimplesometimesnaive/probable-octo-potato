class Solution:
    def combinationSum4(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        l = len(nums)
        # dp: l rows and target + 1 columns
        dp = [0 for i in range(target + 1)]
        
        dp[0] = 1

        for j in range(1, target + 1):
            for i in range(l):
                if j >= nums[i]:
                    dp[j] += dp[j - nums[i]]
        
        return dp[target]

