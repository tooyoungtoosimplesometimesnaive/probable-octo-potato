class Solution(object):
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        result = []
        self.dfs(k, n, 1, [], 0, result)
        return result
    
    def dfs(self, k, n, start, current, current_sum, result):
        if current_sum == n and k == len(current):
            result.append(current)
            return
        if current_sum > n:
            return
        if len(current) > k:
            return
        
        for i in range(start, 10):
            self.dfs(k, n, i + 1, current + [i], current_sum + i, result)

