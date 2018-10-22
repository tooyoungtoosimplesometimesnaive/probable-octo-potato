# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# Some not good but accepted solution.
class Solution(object):
    def __init__(self):
        self.result = float('Inf')
        self.node = None
    def inorderSuccessor(self, root, p):
        """
        :type root: TreeNode
        :type p: TreeNode
        :rtype: TreeNode
        """
        self.do_search(root, p)
        return self.node
    def do_search(self, root, p):
        if root == None:
            return
        if root.val > p.val:
            if self.result > root.val - p.val:
                self.node = root
                self.result = root.val - p.val
            self.do_search(root.left, p)
        else:
            self.do_search(root.right, p)
        
        
