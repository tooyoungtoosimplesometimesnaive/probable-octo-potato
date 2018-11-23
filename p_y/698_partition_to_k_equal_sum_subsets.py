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
        
### Exactly same take 2:
class Solution:
    def canPartitionKSubsets(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        nums_sum = sum(nums)
        if k <= 0 or nums_sum % k != 0:
            return False
        visited = [False for i in range(len(nums))]

        return self.can_partition(nums, k, 0, 0, nums_sum // k, visited)

    def can_partition(self, nums, k, start_index, current_sum, target, visited):
        if k == 0:
            return True
        if current_sum == target:
            return self.can_partition(nums, k - 1, 0, 0, target, visited)

        for i in range(start_index, len(nums)):
            if not visited[i]:
                visited[i] = True
                if self.can_partition(nums, k, i, current_sum + nums[i], target, visited):
                    return True
                visited[i] = False
        return False


# Take 3:
class Solution(object):
    def canPartitionKSubsets(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        if sum(nums) % k != 0:
            return False
        target = sum(nums) // k
        visited = [False for _ in range(len(nums))]

        return self.can_partition(nums, target, k, visited, 0, 0)


    def can_partition(self, nums, target, k, visited, current_sum, start_index):

        if k == 0:
            return True
        if current_sum == target:
            return self.can_partition(nums, target, k - 1, visited, 0, 0)

        i = start_index
        while i < len(nums):
            if not visited[i]:
                if current_sum + nums[i] > target:
                    i += 1
                    continue
                visited[i] = True
                if self.can_partition(nums, target, k, visited, current_sum + nums[i], i + 1):
                    return True
                visited[i] = False
            i += 1
        return False

