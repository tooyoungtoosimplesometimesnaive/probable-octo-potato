class Solution:
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        if len(nums) == 0:
            return 0

        prefix_sum_freq = {0:1}
        s = 0
        result = 0
        for n in nums:
            s += n
            result += prefix_sum_freq.get(s - k, 0)
            prefix_sum_freq[s] = prefix_sum_freq.get(s, 0) + 1
        
        return result

