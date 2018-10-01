class Solution:
    def increasingTriplet(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if len(nums) < 3: return False
        c1, c2 = float('Inf'), float('Inf')
        for k in nums:
            if k <= c1:
                c1 = k
            elif k <= c2:
                c2 = k
            else:
                return True
        return False
