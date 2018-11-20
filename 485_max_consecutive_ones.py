class Solution:
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if nums is None or len(nums) == 0:
            return 0
        
        ones = 1 if nums[0] == 1 else 0
        result = ones
        
        for i in range(1, len(nums)):
            ones = ones + 1 if nums[i] == 1 else 0
            result = max(ones, result)
            
        return result

