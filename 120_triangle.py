class Solution:
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        # index i, next level -> i, i + 1
        if len(triangle) == 0:
            return 0
        if len(triangle) == 1:
            return min(triangle[0])
        
        min_sum = triangle[-1]
        for i in range(len(triangle) - 2, -1, -1): # from len(t) - 2 to 0
            for k in range(len(triangle[i])):
                min_sum[k] = triangle[i][k] + min(min_sum[k], min_sum[k + 1])
        
        return min_sum[0]

