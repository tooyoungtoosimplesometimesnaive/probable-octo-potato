class Solution:
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if len(nums) <= 1:
            return nums
        result = [1] * len(nums)
        
        for i in range(1, len(nums)):
            result[i] = result[i - 1] * nums[i - 1]
        
        #print(result)
        right = nums[-1]
        for i in range(len(nums) - 2, -1, -1):
            result[i] *= right
            right *= nums[i]
        
        return result

