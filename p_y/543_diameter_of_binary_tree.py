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


# Take 2:
# This is super slow.
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root == None:
            return 0
        this_diameter = self.get_height(root.left) + self.get_height(root.right)
        return max(self.diameterOfBinaryTree(root.left), self.diameterOfBinaryTree(root.right), this_diameter)

    def get_height(self, root):
        if root == None:
            return 0
        return 1 + max(self.get_height(root.left), self.get_height(root.right))

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.result = 0
        self.get_height(root)

        return self.result

    def get_height(self, root):
        if root == None:
            return 0
        left = self.get_height(root.left)
        right = self.get_height(root.right)

        self.result = max(self.result, left + right)
        return 1 + max(left, right)
