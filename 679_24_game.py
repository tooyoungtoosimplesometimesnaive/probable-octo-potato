class Solution:
    def judgePoint24(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        return self.dfs(nums)
    
    def dfs(self, nums):
        if len(nums) == 1:
            return abs(nums[0] - 24) < 0.001
        
        for i in range(len(nums)):
            for j in range(len(nums)):
                if i == j: continue
                
                result = []
                for k in range(len(nums)):
                    if k != i and k != j:
                        result.append(nums[k])
                for op in ['+', '-', '*', '/']:
                    if i > j and (op == '+' or op == '*'): # No need to recalculate
                        continue
                    if op == '/' and nums[j] == 0:
                        continue
                    if op == '+':
                        result.append(nums[i] + nums[j])
                    elif op == '-':
                        result.append(nums[i] - nums[j])
                    elif op == '*':
                        result.append(nums[i] * nums[j])
                    else:
                        result.append(nums[i] / nums[j])
                
                    if self.dfs(result):
                        return True
                    result.pop()
            
        return False

