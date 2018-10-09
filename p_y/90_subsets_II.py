class Solution:
    def __init__(self):
        self.result = []

    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        def find(nums, start, current_result):
            print(current_result)
            self.result.append(current_result.copy())

            dedup_set = set()
            for i in range(start, len(nums)):
                if nums[i] not in dedup_set:
                    dedup_set.add(nums[i])
                    current_result.append(nums[i])
                    find(nums, i + 1, current_result)
                    current_result.pop(-1)

        nums.sort()  
        find(nums, 0, [])
        return self.result
