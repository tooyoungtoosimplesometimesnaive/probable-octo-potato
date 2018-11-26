
class Solution:
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Sliding window
        left = 0
        right = 0
        
        zero_count = 0
        result = 0
        while right < len(nums):
            if nums[right] == 0:
                zero_count += 1
                while zero_count > 1:
                    if nums[left] == 0:
                        zero_count -= 1
                    left += 1

            result = max(result, right - left + 1)
            right += 1
        
        return result


# DP solution:
class Solution:
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # longest consecutive ones with at most 1 zero flipping
        dp = [0] * len(nums)

        # longest consecutive ones without flipping
        dp1 = [0] * len(nums)
        dp1[0] = nums[0]

        dp[0] = 1

        result = 1
        for i in range(1, len(nums)):
            dp1[i] = 0 if nums[i] == 0 else 1 + dp1[i - 1]

            dp[i] = dp1[i - 1] + 1 if nums[i] == 0 else 1 + dp[i - 1]
            result = max(dp[i], result)


        return result

