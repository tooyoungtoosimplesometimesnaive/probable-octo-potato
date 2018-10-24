# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        def helper(nums, i, j):
            if i > j:
                return None
            if i == j:
                return TreeNode(nums[i])
            
            root = (i + j) // 2
            root_node = TreeNode(nums[root])
            left = helper(nums, i, root - 1)
            right = helper(nums, root + 1, j)
            root_node.left = left
            root_node.right = right
            return root_node
        
        return helper(nums, 0, len(nums) - 1)

