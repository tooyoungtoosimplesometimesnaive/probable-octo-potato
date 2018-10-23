# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def __init__(self):
        self.result = 0
    def longestConsecutive(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.find(root)
        return self.result
    
    def find(self, root):
        if root == None:
            return 0
        if root.left == None and root.right == None:
            self.result = max(self.result, 1)
            return 1
        left = self.find(root.left)
        right = self.find(root.right)

        left_path = 1
        right_path = 1
        if root.left != None and root.val + 1 == root.left.val:
            left_path += left
        if root.right!= None and root.val + 1 == root.right.val:
            right_path += right
        
        
        self.result = max(self.result, max(left_path, right_path))
        return max(left_path, right_path)

