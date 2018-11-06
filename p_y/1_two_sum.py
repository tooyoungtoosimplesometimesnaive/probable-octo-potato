class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        nums_index = sorted([(x, idx) for x, idx in zip(nums, [i for i in range(len(nums))])])
        i = 0
        j = len(nums) - 1
        while i < j:
            A, A_idx = nums_index[i]
            B, B_idx = nums_index[j]
            if A + B == target:
                return [A_idx, B_idx]
            elif A + B < target:
                i += 1
            else:
                j -= 1
        return []

