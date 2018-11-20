class Solution:
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if nums is None or len(nums) == 0:
            return 0
        if len(nums) == 1:
            return nums[0]
        # money[i] : how much money I will get from 0 to i, robbing index i.
        # money[i]: money[i]
        money = [0] * len(nums)
        money[0] = nums[0]
        if len(nums) >= 2:
            money[1] = nums[1]
        
        if len(nums) == 2:
            return max(money[0], money[1])
        result = max(money[0], money[1])
        for i in range(2, len(nums)):
            for j in range(i - 2 + 1):
                money[i] = max(money[i], money[j] + nums[i])
            result = max(result, money[i])
        #print(money)
        return result

# Take 2: O(N)
class Solution:
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if nums is None or len(nums) == 0:
            return 0
        if len(nums) == 1:
            return nums[0]
        # money[i]: max money from 0 to i
        money = [0] * len(nums)
        money[0] = nums[0]
        result = money[0]
        for i in range(1, len(nums)):
            # money[i - 2] => money[-1] == 0
            money[i] = max(money[i - 2] + nums[i], money[i - 1])
            result = max(result, money[i])

        return result

# O(1) space:
class Solution:
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if nums is None or len(nums) == 0:
            return 0
        if len(nums) == 1:
            return nums[0]
        # money[i]: max money from 0 to i
        prev_money = 0
        curr_money = 0
        for i in range(len(nums)):
            temp = curr_money
            curr_money = max(prev_money + nums[i], curr_money)
            prev_money = temp
        return curr_money

