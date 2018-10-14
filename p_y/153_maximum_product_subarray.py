class Solution:
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        tmp_max = nums[0]
        tmp_min = nums[0]
        result = nums[0]
        
        for i in range(1, len(nums)):
            n = nums[i]
            curr_max = max(n, n * tmp_max, n * tmp_min)
            curr_min = min(n, n * tmp_max, n * tmp_min)
            result = max(result, curr_max, curr_min)
            #print("{},{},{},{}".format(n, curr_max, curr_min, result))
            tmp_max = curr_max
            tmp_min = curr_min
            #print(result)
        return result


