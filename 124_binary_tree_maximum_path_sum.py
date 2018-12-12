# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def __init__(self):
        self.result = float('-inf')

    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.find_path(root)
        
        return self.result
    
    def find_path(self, root):
        if root == None:
            return 0
        left = self.find_path(root.left)
        right = self.find_path(root.right)
        
        self.result = max(self.result, left + right + root.val, root.val + left, root.val + right, root.val)
        
        left_path = root.val if left < 0 else root.val + left
        right_path = root.val if right < 0 else root.val + right
            
        return max(left_path, right_path)
        
        
        
