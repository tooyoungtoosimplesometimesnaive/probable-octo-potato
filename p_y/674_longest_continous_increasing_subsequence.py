class Solution:
    def findLengthOfLCIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        m = [1 for i in range(len(nums))]
        result = 1
        for i, n in enumerate(nums):
            if i == 0: continue
            if n > nums[i - 1]:
                m[i] = m [i - 1] + 1
                result = max(result, m[i])
        return result

# Take 2:
class Solution:
    def findLengthOfLCIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if nums == None or len(nums) == 0:
            return 0
        length = [1] * len(nums)
        result = 1
        for i in range(1, len(nums)):
            if nums[i] > nums[i - 1]:
                length[i] = length[i - 1] + 1
            else:
                length[i] = 1
            result = max(result, length[i])
        return result

