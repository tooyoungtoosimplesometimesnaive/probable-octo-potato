class Solution:
    def canIWin(self, maxChoosableInteger, desiredTotal):
        """
        :type maxChoosableInteger: int
        :type desiredTotal: int
        :rtype: bool
        """
        if (1 + maxChoosableInteger) * maxChoosableInteger // 2 < desiredTotal:
            # if sum(1..nums) < desiredTotal, then it should return false
            return False
        self.mem = {}
        nums = [i for i in range(1, maxChoosableInteger + 1)]
        return self.helper(nums, desiredTotal)
        
    def helper(self, nums, desiredTotal):
        key = str(nums)
        if key in self.mem:
            return self.mem[key]

        if desiredTotal <= nums[-1]:
            return True
        
        for i in range(len(nums)):
            if not self.helper(nums[:i] + nums[i + 1:], desiredTotal - nums[i]):
                self.mem[key] = True
                return True
        self.mem[key] = False
        return False

