class Solution:
    def nextGreaterElements(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        stack = []
        i = 2 * n - 1
        result = [0 for _ in range(n)]
        while i >= 0:
            index = i % n
            e = nums[index]
            if len(stack) == 0:
                result[index] = -1
                stack.append(e)
            
            elif e < stack[-1]:
                result[index] = stack[-1]
                stack.append(e)
            else:
                while len(stack) > 0 and e >= stack[-1]:
                    stack.pop()
                result[index] = -1 if len(stack) == 0 else stack[-1]
                stack.append(e)
            i -= 1
        return result

