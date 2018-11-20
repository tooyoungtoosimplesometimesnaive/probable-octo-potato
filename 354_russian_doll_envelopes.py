from functools import cmp_to_key
from bisect import bisect_left

class Solution:

    def maxEnvelopes(self, envelopes):
        """
        :type envelopes: List[List[int]]
        :rtype: int
        """
        def env_cmp(env1, env2):
            x1, y1 = env1
            x2, y2 = env2
            if x1 != x2:
                return 1 if x1 > x2 else -1
            else:
                return 1 if y1 < y2 else -1 if y1 > y2 else 0
        
        if envelopes == None or len(envelopes) == 0:
            return 0
        # Sort the envelopes, x from small to large, if x equals, then y from large to small
        # Then get the y
        sorted_envs = list(map(lambda k: k[1], sorted(envelopes, key=cmp_to_key(env_cmp))))

        result = 0
        #longest increasing subsequence:
        nums = []
        for i in range(len(sorted_envs)):
            index = bisect_left(nums, sorted_envs[i])
            if index >= len(nums):
                nums.append(sorted_envs[i])
            else:
                nums[index] = sorted_envs[i]
            result = max(result, len(nums))
        
        #print(sorted_envs)
        return result

