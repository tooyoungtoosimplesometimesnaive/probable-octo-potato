class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        result = []
        candidates.sort()
        self.dfs(candidates, target, [], 0, 0, result)
        return result
    
    
    def dfs(self, candidates, target, current, current_sum, start, result):
        if current_sum == target:
            result.append(current)
            return
        if current_sum > target:
            return
        
        for i in range(start, len(candidates)):
            c = candidates[i]
            self.dfs(candidates, target, current + [c], current_sum + c, i, result)
