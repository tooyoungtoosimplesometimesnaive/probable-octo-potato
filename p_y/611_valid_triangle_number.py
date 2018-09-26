class Solution:
    def triangleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()

        result = 0
        if len(nums) <= 2:
            return 0
        i = len(nums) - 1
        while i >= 2:
            l = 0
            r = i - 1
            while l < r:
                if nums[l] + nums[r] > nums[i]:
                    result += r - l
                    r -= 1
                else:
                    l += 1
            i -= 1
        return result

            
