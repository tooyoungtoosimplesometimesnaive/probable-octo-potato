# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def __init__(self):
        self.count = 0
    def countUnivalSubtrees(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.is_unival(root)
        return self.count
    
    def is_unival(self, root):
        if root == None:
            return True

        left = self.is_unival(root.left)
        right = self.is_unival(root.right)
        
        if left and right:
            if root.left != None and root.left.val != root.val:
                return False
            
            if root.right != None and root.right.val != root.val:
                return False
            
            self.count += 1
            return True
        
        else:
            return False

