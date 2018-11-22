class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return max(nums[0], nums[1])
        
        return max(self.rob_range(nums, 0, len(nums) - 2), self.rob_range(nums, 1, len(nums) - 1))
        
    def rob_range(self, nums, start, end):
        dp = [0] * len(nums)
        dp[start] = nums[start]
        dp[start + 1] = max(nums[start], nums[start + 1])
        # dp[i] = max(dp[i - 2] + nums[i], dp[i - 1])
        for i in range(start + 2, end + 1):
            dp[i] = max(dp[i - 2] + nums[i], dp[i - 1])
        return dp[end]
        

