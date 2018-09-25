# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def findLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        def is_leaf(n):
            return n != None and n.left == None and n.right == None

        # return true if root is leaf
        def dfs(root, leaf_list):
            if root == None:
                return
            if is_leaf(root):
                leaf_list.append(root.val)
                return
            
            if is_leaf(root.left):
                if root.left != None:
                    leaf_list.append(root.left.val)
                root.left = None
            else:
                dfs(root.left, leaf_list)
            
            if is_leaf(root.right):
                if root.right != None:
                    leaf_list.append(root.right.val)
                root.right = None
            else:
                dfs(root.right, leaf_list)

        result = []
        if root == None:
            return result
        while root.left != None or root.right != None:
            level = []
            dfs(root, level)
            result.append(level)
            
        if root.left == None and root.right == None:
            result.append([root.val])
        return result


