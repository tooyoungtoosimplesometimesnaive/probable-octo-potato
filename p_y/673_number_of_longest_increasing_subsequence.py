class Solution:
    def findNumberOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) <= 0: return 0;
        M = [1 for i in range(len(nums))]
        count = [1 for i in range(len(nums))]
        result = 1
        for i, n in enumerate(nums):
            for k in range(i):
                if n > nums[k]:
                    if M[k] >= M[i]:
                        M[i] = M[k] + 1
                        count[i] = count[k]
                    elif M[k] + 1 == M[i]:
                        count[i] += count[k]
                        
        result = max(M)
        # print(result)
        # print(M)
        # print(count)
        return sum([c for i, c in enumerate(count) if M[i] == result])

       
