class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        def reverse(nums, start, end):
            while start < end:
                nums[start], nums[end] = nums[end], nums[start]
                start += 1
                end -= 1
        
        k %= len(nums)
        reverse(nums, 0, len(nums) - 1 - k)
        reverse(nums, len(nums) - k, len(nums) - 1)
        reverse(nums, 0, len(nums) - 1)

