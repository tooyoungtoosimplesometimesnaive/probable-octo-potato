class Solution:
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        ans = []
        def per(nums, i):
            if i >= len(nums):
                #print(nums)
                ans.append(nums.copy())
                return
            dedup_set = set()
            for k in range(i, len(nums)):
                if nums[k] not in dedup_set:
                    dedup_set.add(nums[k])
                    nums[i], nums[k] = nums[k], nums[i]
                    per(nums, i + 1)
                    nums[i], nums[k] = nums[k], nums[i]

        
        per(nums, 0)
        return ans
            
