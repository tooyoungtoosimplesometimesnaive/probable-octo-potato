class Solution:
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        def do_perm(nums, i, result):
            if i == len(nums):
                result.append(nums.copy())
                return
            for k in range(i, len(nums)):
                #print(nums)
                nums[k], nums[i] = nums[i], nums[k]
                do_perm(nums, i + 1, result)
                nums[k], nums[i] = nums[i], nums[k]
        result = []
        do_perm(nums, 0, result)
        return result

        
