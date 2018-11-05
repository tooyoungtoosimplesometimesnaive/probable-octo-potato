class Solution(object):
    def findPairs(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        nums.sort()
        result = 0
        if k < 0:
            return 0
        
        start = 0
        end = 0
        while start < len(nums) and end < len(nums):
            if start == end or nums[start] + k > nums[end]:
                # end needs to be bigger
                end += 1
            elif nums[start] + k < nums[end]:
                start += 1
            else:
                result += 1
                start += 1
                while end < len(nums) - 1 and nums[end] == nums[end + 1]:
                    end += 1
                end += 1
        return result

