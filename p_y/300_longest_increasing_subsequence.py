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

