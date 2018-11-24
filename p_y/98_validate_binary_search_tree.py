# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def __init__(self):
        self.prev = None

    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        #if root == None:
        #    return True
    
        return self.is_valid(root)
    
    def is_valid(self, root):
        if root == None:
            return True
        if not self.is_valid(root.left):
            return False
        if self.prev != None and self.prev.val >= root.val:
            print("here")
            return False
        self.prev = root
        # if prev == None:
        #     print("None")
        # else:
        #     print("{}".format(prev.val))
        return self.is_valid(root.right)
        
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        return self.is_valid(root, -9223372036854775807, 9223372036854775807)
    
    def is_valid(self, root, min_value, max_value):
        if root == None:
            return True
        if root.val >= max_value or root.val <= min_value:
            return False
        return self.is_valid(root.left, min_value, root.val) and self.is_valid(root.right, root.val, max_value)

  

# Take 2:
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def __init__(self):
        self.prev = None
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root == None:
            return True

        is_left_valid = self.isValidBST(root.left)

        if self.prev != None:
            if self.prev >= root.val:
                return False

        self.prev = root.val
        is_right_valid = self.isValidBST(root.right)

        return is_left_valid and is_right_valid

