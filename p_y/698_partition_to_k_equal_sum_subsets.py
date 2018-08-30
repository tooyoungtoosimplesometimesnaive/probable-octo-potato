class Solution:
    def canPartitionKSubsets(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        nums_sum = sum(nums)
        #print(nums_sum)
        if k <= 0 or nums_sum % k != 0:
            return False
        visited = [False for i in range(len(nums))]
        return self.canPartition(nums, k, visited, 0, 0, nums_sum / k)
        #print(visited)
        #return False
    
    def canPartition(self, nums, k, visited, start_idx, cur_sum, target):
        if k == 0:
            return True
        if cur_sum == target:
            return self.canPartition(nums, k - 1, visited, 0, 0, target)
        
        i = start_idx
        while i < len(nums):
            if not visited[i]:
                visited[i] = True
                if self.canPartition(nums, k, visited, i + 1, cur_sum + nums[i], target):
                    return True
                visited[i] = False
            i += 1
            
        return False
        
