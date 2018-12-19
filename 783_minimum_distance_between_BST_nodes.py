# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def __init__(self):
        self.result = float('inf')
        self.prev = None
        
    def minDiffInBST(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.inorder(root)
        return self.result
    
    def inorder(self, root):
        if root == None:
            return
        
        self.inorder(root.left)

        if self.prev != None:
            self.result = min(self.result, abs(root.val - self.prev.val))
        
        self.prev = root
        self.inorder(root.right)

