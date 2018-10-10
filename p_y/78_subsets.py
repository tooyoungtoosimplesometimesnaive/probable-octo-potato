class Solution:
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        def get(nums, start, current_result, results):
            results.append(current_result.copy())
            
            for i in range(start, len(nums)):
                current_result.append(nums[i])
                get(nums, i + 1, current_result, results)
                current_result.pop(-1)
            
        results = []
        get(nums, 0, [], results)
        return results
