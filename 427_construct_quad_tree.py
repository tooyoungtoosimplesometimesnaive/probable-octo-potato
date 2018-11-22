"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""
class Solution:
    def construct(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: Node
        """
        row = len(grid)
        col = len(grid[0])
        return self.construct_helper(grid, 0, row, 0, col)
        
    def construct_helper(self, grid, row_start, row_end, col_start, col_end):
        is_same, value = self.is_all_same(grid, row_start, row_end, col_start, col_end)
        if is_same:
            return Node(value, True, None, None, None, None)
        
        top_left = self.construct_helper(grid, row_start, (row_start + row_end) // 2, col_start, (col_start + col_end) // 2)
        top_right = self.construct_helper(grid, row_start, (row_start + row_end) // 2, (col_start + col_end) // 2, col_end)
        
        bottom_left = self.construct_helper(grid, (row_start + row_end) // 2, row_end, col_start, (col_start + col_end) // 2)
        bottom_right = self.construct_helper(grid, (row_start + row_end) // 2, row_end, (col_start + col_end) // 2, col_end)
        
        return Node(True, False, top_left, top_right, bottom_left, bottom_right)
        
    
    def is_all_same(self, grid, row_start, row_end, col_start, col_end):
        value = grid[row_start][col_start]
        
        for i in range(row_start, row_end):
            for j in range(col_start, col_end):
                if value != grid[i][j]:
                    return (False, -1)
        return (True, value == 1)

