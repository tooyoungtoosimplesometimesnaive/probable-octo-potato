# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def __init__(self):
        self.prev = None
        self.count = 1
        self.max = 0

    def findMode(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        result = []
        self.in_order(root, result)
        return result
    
    def in_order(self, root, result):
        if root == None:
            return
        self.in_order(root.left, result)
        if self.prev != None:
            if self.prev == root.val:
                self.count += 1
            else:
                self.count = 1
        
        if self.count > self.max:
            # print(self.count, self.max)
            self.max = self.count
            result.clear()
            result.append(root.val)
        elif self.count == self.max:
            result.append(root.val)

        self.prev = root.val
        self.in_order(root.right, result)

