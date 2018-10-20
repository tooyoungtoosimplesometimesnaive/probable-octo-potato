# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# Notice: if the total number of nodes is N, then on average this is O(n / 2)
# Worst case is O(n - 1)
# XD
class Solution:
    def __init__(self):
        self.result = 0
    def countNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def get_height(r):
            if r == None:
                return 0
            return get_height(r.left) + 1
        
        def count_last_row(r, current_level, h):
            if current_level != h - 1:
                count_last_row(r.left, current_level + 1, h)
                count_last_row(r.right, current_level + 1, h)
            else:
                if r.left != None: self.result += 1
                if r.right != None: self.result += 1
    
    
        h = get_height(root)
        if h <= 1:
            return h
        count_last_row(root, 1, h)
        return self.result + 2 ** (h - 1) - 1
        
        
# Better solution: O(logN * logN)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def __init__(self):
        self.result = 0

    def get_height(self, root):
        if root == None:
            return 0
        return self.get_height(root.left) + 1

    def countNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root == None:
            return 0
        h_left = self.get_height(root.left)
        h_right = self.get_height(root.right)
        if h_left != h_right:
            return self.countNodes(root.left) + 1 + 2 ** h_right - 1
        else:
            return self.countNodes(root.right) + 1 + 2 ** h_left - 1

