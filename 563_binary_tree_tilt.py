# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def __init__(self):
        self.result = 0

    def findTilt(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.find_tilt(root)
        return self.result
    
    def find_tilt(self, root):
        if root == None:
            return 0
        left = self.find_tilt(root.left)
        right = self.find_tilt(root.right)
        
        self.result += abs(left - right)
        
        return left + right + root.val
        

