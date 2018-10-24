# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def __init__(self):
        self.result = 0

    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def get_depth(root):
            if root == None:
                self.result = max(self.result, 0)
                return 0

            left = get_depth(root.left)
            right = get_depth(root.right)
            d = left + right + 1
            self.result = max(self.result, d)
            return max(left, right) + 1
        if root == None:
            return 0
        get_depth(root)
        return self.result - 1

