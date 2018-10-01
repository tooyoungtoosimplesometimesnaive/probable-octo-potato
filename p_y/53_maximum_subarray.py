class Solution:
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) <= 0: return None
        M = [0 for i in range(len(nums))]
        M[0] = nums[0]
        result = M[0]
        for i, n in enumerate(nums):
            if i == 0: continue
            M[i] = M[i - 1] + n if M[i - 1] + n > n else n
            result = max(result, M[i])
        
        return result
