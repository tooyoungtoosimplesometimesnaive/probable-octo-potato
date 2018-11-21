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

# take 2:
class Solution:
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if nums == None or len(nums) == 0:
            return 0
        arr_max = [0] * len(nums)
        arr_min = [0] * len(nums)
        arr_max[0] = nums[0]
        arr_min[0] = nums[0]
        result = nums[0]

        for i in range(1, len(nums)):
            arr_max[i] = max(arr_max[i - 1] * nums[i], arr_min[i - 1] *nums[i], nums[i])
            arr_min[i] = min(arr_max[i - 1] * nums[i], arr_min[i - 1] *nums[i], nums[i])
            result = max(result, arr_max[i], arr_min[i])

        return result

