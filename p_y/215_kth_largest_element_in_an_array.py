# an ugly solution:
class Solution:
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        m = self.quick_select(nums, k)
        #print(m)
        #print(nums)
        return m

    def quick_select(self, nums, k):
        return self.quick_select_helper(nums, 0, len(nums) - 1, k)

    def quick_select_helper(self, nums, left, right, k):
        if left >= right:
            return nums[left]
        #if left < right:
        p = self.partition(nums, left, right)
        if p == len(nums) - k:
            return nums[p]
        elif p > len(nums) - k:
            return self.quick_select_helper(nums, left, p - 1, k)
        else:
            return self.quick_select_helper(nums, p + 1, right, k)
        #self.quick_select_helper(nums, left, p - 1, k)
        #self.quick_select_helper(nums, p + 1, right, k)

    def partition(self, nums, left, right):
        o_left = left
        pivot = nums[left]
        left += 1
        
        while left <= right:
            if pivot >= nums[left]:
                left += 1
            else:
                tmp = nums[left]
                nums[left] = nums[right]
                nums[right] = tmp
                right -= 1

        tmp = nums[left - 1]
        nums[left - 1] = pivot
        nums[o_left] = tmp
        #print("---" + str(nums) + " p = " + str(left) + " right = " + str(right))
        return left - 1

