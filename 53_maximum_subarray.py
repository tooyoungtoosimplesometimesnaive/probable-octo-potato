class Solution:
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        if nums is None or len(nums) == 0:
            return 0
        
        result = nums[0]
        sums = [result] * len(nums)
        
        # sums[i] : maximum subarray till index i, including index i
        # sums[i] = nums[i] if nums[i] + sums[i - 1] < nums[i] (sums[i] < 0)
        #         = nums[i] + sums[i - 1] otherwise
        for i in range(1, len(nums)):
            if nums[i] + sums[i - 1] < nums[i]:
                sums[i] = nums[i]
            else:
                sums[i] = sums[i - 1] + nums[i]
            result = max(result, sums[i])
    
        return result

