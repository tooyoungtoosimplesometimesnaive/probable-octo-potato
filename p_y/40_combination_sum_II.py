class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        candidates.sort()
        result = []
        self.dfs(0, candidates, target, [], 0, result)
        return result
    
    def dfs(self, start, candidates, target, current, current_sum, result):
        #base case:

        if current_sum == target:
            result.append(current)
            return
        if current_sum > target:
            return
        
        for i in range(start, len(candidates)):
            if i == start or candidates[i] != candidates[i - 1]:
                c = candidates[i]
                self.dfs(i + 1, candidates, target, current + [c], current_sum + c, result)

