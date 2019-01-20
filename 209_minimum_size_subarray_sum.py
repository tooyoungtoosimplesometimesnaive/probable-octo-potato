class Solution:
    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        slow = 0
        fast = 0
        current = 0
        result = float('inf')
        while fast < len(nums):
            current += nums[fast]
            while slow < fast and current - nums[slow] >= s:
                current -= nums[slow]
                slow += 1
            if current >= s:
                result = min(result, fast - slow + 1)
                # print(fast, slow, result)

            fast += 1

        return 0 if result == float('inf') else result

