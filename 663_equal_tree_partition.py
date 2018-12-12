# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def __init__(self):
        self.sum_count = collections.defaultdict(int)

    def checkEqualTree(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        s = self.sum_up(root)
        
        if s == 0:
            return self.sum_count[s] > 1
        
        return s % 2 == 0 and (s // 2) in self.sum_count
        
    def sum_up(self, root):
        if root == None:
            return 0
        
        left = self.sum_up(root.left)
        right = self.sum_up(root.right)
        self.sum_count[left + root.val + right] += 1
        
        return left + root.val + right

