class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        min_distance = float('inf')
        result = 0
        for i in range(len(nums) - 2):
            j = i + 1
            k = len(nums) - 1
            while j < k:
                s = nums[i] + nums[j] + nums[k]
                if s == target:
                    return target
                elif s < target:
                    j += 1
                else:
                    k -= 1
                if min_distance > abs(target - s):
                    result = s
                    min_distance = abs(target - s)
                
        return result

