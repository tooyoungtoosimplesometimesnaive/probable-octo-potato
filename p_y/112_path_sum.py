# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        def find_path(root, current_sum, sum):
            if root == None:
                return False
            if root.left == None and root.right == None:
                if root.val + current_sum == sum:
                    return True
                else:
                    return False
            return find_path(root.left, current_sum + root.val, sum) or find_path(root.right, current_sum + root.val, sum)
        
        return find_path(root, 0, sum)

