class Solution:
    def __init__(self):
        self.result = []

    def findSubsequences(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        def find(nums, start, current_result):
            if len(current_result) >= 2:
                self.result.append(current_result.copy())

            i = start
            dedup_set = set()
            while i < len(nums):

                if (nums[i] not in dedup_set) and (len(current_result) == 0 or current_result[-1] <= nums[i]):
                    dedup_set.add(nums[i])


                    current_result.append(nums[i])
                    find(nums, i + 1, current_result)
                    current_result.pop(-1)
                i += 1

        current_result = []
        find(nums, 0, current_result)

        return self.result


