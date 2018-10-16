class Solution:
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0

        tmp_max, tmp_min = nums[0], nums[0]
        result = nums[0]
        for n in nums[1:]:
            cur_max = max(n, tmp_max * n, tmp_min * n)
            cur_min = min(n, tmp_max * n, tmp_min * n)
            result = max(result, cur_max, cur_min)
            tmp_max = cur_max
            tmp_min = cur_min
        return result
