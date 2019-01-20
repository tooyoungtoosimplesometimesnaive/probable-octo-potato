class NumMatrix(object):

    def __init__(self, matrix):
        """
        :type matrix: List[List[int]]
        """
        self.m = len(matrix)
        if self.m == 0:
            return
        self.n = len(matrix[0])
        if self.n == 0:
            return
        self.tree = [[0 for _ in range(self.n + 1)] for _ in range(self.m + 1)]
        
        self.nums = [[0 for _ in range(self.n)] for _ in range(self.m)]
        
        for i in range(self.m):
            for j in range(self.n):
                self.update(i, j, matrix[i][j])
        

    def update(self, row, col, val):
        """
        :type row: int
        :type col: int
        :type val: int
        :rtype: void
        """
        if self.m == 0 or self.n == 0:
            return
        
        diff = val - self.nums[row][col]
        self.nums[row][col] = val
        i = row + 1
        j = col + 1
        while i <= self.m:
            while j <= self.n:
                self.tree[i][j] += diff
                j += (j & (-j))
            i += (i & (-i))
            j = col + 1

    def sumRegion(self, row1, col1, row2, col2):
        """
        :type row1: int
        :type col1: int
        :type row2: int
        :type col2: int
        :rtype: int
        """
        if self.m == 0 or self.n == 0:
            return 0
        # print('in sum region')
        # for i in range(self.m + 1):
        #     print(self.tree[i])
        return self.get_sum(row2 + 1, col2 + 1) - self.get_sum(row1, col2 + 1) - self.get_sum(row2 + 1, col1) + self.get_sum(row1, col1)
        
        
    def get_sum(self, row, col):
        i = row
        j = col
        result = 0
        while i > 0:
            while j > 0:
                result += self.tree[i][j]
                j -= (j & (-j))
            i -= (i & (-i))
            j = col
        return result

# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# obj.update(row,col,val)
# param_2 = obj.sumRegion(row1,col1,row2,col2)
