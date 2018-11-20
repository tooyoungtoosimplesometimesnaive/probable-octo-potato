class Solution:
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0: return 0
        M = [1 for i in range(len(nums))]
        result = 1
        for i, n in enumerate(nums):
            this_max = 1
            for k in range(i):
                if n > nums[k]:
                    this_max = max(this_max, M[k] + 1)
            M[i] = this_max
            result = max(result, M[i])
        return result


# Take 2, use binary search.
from bisect import bisect_left
class Solution:
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if nums == None or len(nums) == 0:
            return 0
        LIS = []
        result = 1
        for i in range(len(nums)):
            index = bisect_left(LIS, nums[i])
            # print(index)
            # print(LIS)
            if index >= len(LIS):
                LIS.append(nums[i])
            else:
                LIS[index] = nums[i]

            result = max(result, len(LIS))
        return result
