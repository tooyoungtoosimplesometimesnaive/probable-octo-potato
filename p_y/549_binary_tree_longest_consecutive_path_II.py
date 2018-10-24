# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def __init__(self):
        self.result = 1

    def longestConsecutive(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root == None:
            return 0
        self.find(root)
        return self.result
        
    def find(self, root):
        if root == None:
            return (0, 0)
        left_inc, left_dec = self.find(root.left)
        right_inc, right_dec = self.find(root.right)
        
        dec = 1
        inc = 1
        if root.left != None:
            if root.val == root.left.val + 1:
                dec = max(dec, left_dec + 1)
                self.result = max(self.result, dec)
            elif root.val == root.left.val - 1:
                inc = max(inc, left_inc + 1)
                self.result = max(self.result, inc)
            # else:
            #     dec = max(dec, 1)
            #     inc = max(inc, 1)
        if root.right != None:
            if root.val == root.right.val + 1:
                dec = max(dec, right_dec + 1)
                self.result = max(self.result, dec)
            elif root.val == root.right.val - 1:
                inc = max(inc, right_inc + 1)
                self.result = max(self.result, inc)
            # else:
            #     dec = max(dec, 1)
            #     inc = max(inc, 1)
        # Special case:
        if root.left != None and root.right != None:
            if root.val == root.right.val + 1 and root.val == root.left.val - 1:
                self.result = max(self.result, right_dec + left_inc + 1)
            if root.val == root.right.val - 1 and root.val == root.left.val + 1:
                self.result = max(self.result, left_dec + right_inc + 1)
        return (inc, dec)

