class Solution:
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
#         m = collections.defaultdict(int)
#         for n in nums:
#             m[n] += 1
        
#         for k, v in m.items():
#             if v == 1:
#                 return k
#         return -1
        ones, twos = 0, 0
        for n in nums:
            ones = (ones ^ n) & ~twos
            twos = (twos ^ n) & ~ones
        return ones
