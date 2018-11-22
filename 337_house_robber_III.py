# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def rob(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        # stolen[n] max money with node n stolen
        # not_stolen[n] max money with node n not stolen
        
        # stolen[n]     = max(not_stolen[n.left] + not_stolen[n.right]) + n.val
        # not_stolen[n] = max(stolen[n.left], not_stolen[n.left]) + max(stolen[n.right], not_stolen[n.right]
        
        # answer = max(stolen[root], not_stolen[root])
        if root == None:
            return 0
        stolen = {}
        not_stolen = {}
        self.calculate(root, stolen, not_stolen)

        return max(stolen[root], not_stolen[root])
        
    def calculate(self, root, stolen, not_stolen):
        if root == None:
            return
        if root.left == None and root.right == None:
            stolen[root] = root.val
            not_stolen[root] = 0
            return
        
        self.calculate(root.left, stolen, not_stolen)
        self.calculate(root.right, stolen, not_stolen)
        
        if root.left == None or root.right == None:
            next_node = root.right if root.left == None else root.left
            
            stolen[root] = not_stolen[next_node] + root.val
            not_stolen[root] = max(stolen[next_node], not_stolen[next_node])
        
        else:
            stolen[root] = not_stolen[root.left] + not_stolen[root.right] + root.val
            not_stolen[root] = max(stolen[root.left], not_stolen[root.left]) + max(stolen[root.right], not_stolen[root.right])
        

