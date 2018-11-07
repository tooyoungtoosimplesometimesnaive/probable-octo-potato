class Solution:
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        if len(height) == 0:
            return 0

        left_max = [0 for _ in range(len(height))]
        right_max = [0 for _ in range(len(height))]
        
        left_max[0] = height[0]
        for i in range(1, len(height)):
            left_max[i] = max(left_max[i - 1], height[i])

        right_max[len(height) - 1] = height[len(height) - 1]
        for j in range(len(height) - 2, 0, -1):
            right_max[j] = max(right_max[j + 1], height[j])
        
        # print(left_max)
        # print(right_max)
        result = 0
        for k in range(1, len(height) - 1):
            result += min(right_max[k], left_max[k]) - height[k]
            
        return result

