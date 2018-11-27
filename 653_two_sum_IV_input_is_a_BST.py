class Solution:
    def findTarget(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: bool
        """
        val_set = set()
        return self.find(root, k, val_set)
    
    def find(self, root, k, val_set):
        if root == None:
            return False
        if k - root.val in val_set:
            return True
        val_set.add(root.val)
        return self.find(root.left, k, val_set) or self.find(root.right, k, val_set)

