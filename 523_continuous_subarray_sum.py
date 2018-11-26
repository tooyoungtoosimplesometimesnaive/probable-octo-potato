class Solution:
    def checkSubarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        if len(nums) < 2:
            return False
        
        prefix_sum = [nums[0]]
        for i in range(1, len(nums)):
            prefix_sum += [prefix_sum[-1] + nums[i]]
        
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                
                s = prefix_sum[j] - prefix_sum[i] + nums[i]
                
                if s == k or (k != 0 and s % k == 0):
                    return True
        
        return False

