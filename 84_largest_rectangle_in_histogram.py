class Solution:
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        if len(heights) == 0:
            return 0
        stack = []
        result = heights[0]
        stack.append(0)

        for i in range(1, len(heights)):
            h = heights[i]
            while len(stack) > 0 and heights[stack[-1]] > h:
                cur_id = stack.pop()
                left = 0 if len(stack) == 0 else stack[-1] + 1
                result = max(result, heights[cur_id] * (i - left))
            stack.append(i)

        while len(stack) > 0:
            cur_id = stack.pop()
            left = 0 if len(stack) == 0 else stack[-1] + 1
            result = max(result, heights[cur_id] * (len(heights) - left))

        return result

