class NumArray:

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.n = len(nums)
        if self.n == 0:
            return

        self.tree = [0 for _ in range(self.n + 1)]
        self.array = [0 for _ in range(self.n)]
        
        for i in range(self.n):
            self.update(i, nums[i])

    def update(self, i, val):
        """
        :type i: int
        :type val: int
        :rtype: void
        """
        if self.n == 0:
            return
        
        diff = val - self.array[i]
        self.array[i] = val
        
        index = i + 1
        while index <= self.n:
            self.tree[index] += diff
            index += (index & (-index))
        

    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        if self.n == 0:
            return 0
        return self.get_sum(j + 1) - self.get_sum(i)
    
    def get_sum(self, i):
        result = 0
        index = i
        while index > 0:
            result += self.tree[index]
            index -= (index & (-index))
        
        return result
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(i,val)
# param_2 = obj.sumRange(i,j)
