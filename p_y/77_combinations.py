class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
    
        result = []
        self.dfs(1, n, k, [], result)
        return result

    def dfs(self, start, n, k, current, result):
        if len(current) == k:
            result.append(current)
            return
        
        for i in range(start, n + 1):
            self.dfs(i + 1, n, k, current + [i], result)

