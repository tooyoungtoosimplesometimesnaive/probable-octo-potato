# This is a TLE in python

class Solution:
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if nums == None or len(nums) == 0:
            return False
        can_jump = [False] * len(nums)
        can_jump[-1] = True
        
        for i in range(len(nums) - 2, -1, -1):
            # the furthest step is min(i + nums[i], len(nums) - 1)
            for j in range(i + 1, min(i + nums[i], len(nums) - 1) + 1):
                
                if can_jump[j]:
                    can_jump[i] = True
                    break
        
        return can_jump[0]


# this greedy O(N) solution:
class Solution:
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if nums == None or len(nums) == 0:
            return False

        n = len(nums)

        reach = 0
        i = 0
        while i < n and i <= reach:
            reach = max(reach, i + nums[i])
            i += 1

        #print(reach)
        return i == n

