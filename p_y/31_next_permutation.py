class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        if len(nums) <= 1:
            return
        i = len(nums) - 1 - 1
        while i >= 0:
            if nums[i] < nums[i + 1]:
                break
            i -= 1
        if i == -1:
            nums.sort()
            return
        j = len(nums) - 1
        while j > i:
            if nums[j] > nums[i]:
                nums[j], nums[i] = nums[i], nums[j]
                break
            j -= 1
        self.reverse_nums(nums, i + 1, len(nums) - 1)
        
    def reverse_nums(self, nums, i, j):
        while j >= i:
            nums[i], nums[j] = nums[j], nums[i]
            j -= 1
            i += 1

