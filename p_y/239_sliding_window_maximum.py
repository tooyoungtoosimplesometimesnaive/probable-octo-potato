class Solution:
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        res = []
        window = []
        
        for i in range(0, len(nums)):
            #print(i)
            while len(window) > 0 and window[0] < i - k + 1:
                window.pop(0)
            #print(window)
            while len(window) > 0 and nums[window[-1]] < nums[i]:
                window.pop(-1)
            #print(window)
            window.append(i)
            #print("----")
            if i >= k - 1:
                res.append(nums[window[0]])
        return res
        

