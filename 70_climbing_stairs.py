class Solution:
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 1:
            return 1
        ways = [0] * (n + 1)
        ways[1] = 1
        ways[2] = 2
        
        # ways[n] = ways[n - 1] + ways[n - 2]
        
        for i in range(3, n + 1): # 3 to n
            ways[i] = ways[i - 1] + ways[i - 2]
        
        return ways[n]

